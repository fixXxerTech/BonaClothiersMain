import json
import string
import random

from . import forms
from . import models
from pprint import pprint
from .helpers import EmailManager
from django.contrib import messages
from django.http import JsonResponse
from os.path import join as join_path
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.views.generic.base import View as custom_view
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import views as auth_views, authenticate, login, logout, get_user_model


# GET Current date and time.
# ---------------------------
Todays_Date = timezone.now()
Todays_Date = Todays_Date.strftime("%Y")

# GET Authenticated user model.
# -----------------------------
Authenticated_manager = get_user_model()

# SET admin acess title.
# -----------------------
panel_name = "Prime Access"


class SignUpPhonenumberValidationView(custom_view):
        # Checks the Userprofile Model if the phonenumber is present establishing it is unique

    def post(self, request):

        request_data = json.loads(request.body)
        userphonenumber = request_data['userphonenumber']

        if str(userphonenumber)[0] == '+':
            userphonenumber_clean = str(userphonenumber)[1:]

            if not str(userphonenumber_clean).isnumeric():
                return JsonResponse(
                    {
                        'userphone_error':
                        '&#x25cf; Invalid phone number format'
                    },
                    status=400)

            if models.UserProfile.objects.filter(
                    userphonenumber=userphonenumber).exists():
                return JsonResponse(
                    {
                        'userphone_error':
                        '&#x25cf; sorry phonenumber in use, choose another one'
                    },
                    status=409)
        else:
            if not str(userphonenumber).isnumeric():
                return JsonResponse(
                    {
                        'userphone_error':
                        '&#x25cf; Invalid phone number format'
                    },
                    status=400)

            if models.UserProfile.objects.filter(
                    userphonenumber=userphonenumber).exists():
                return JsonResponse(
                    {
                        'userphone_error':
                        '&#x25cf; sorry phonenumber in use, choose another one'
                    },
                    status=409)
        return JsonResponse({'userphone_valid': True}, status=200)


class SignUpEmailValidationView(custom_view):
        # This checks the actual django auth model inside django for the email address returned by the request to establish it is unique

    def post(self, request):
        request_data = json.loads(request.body)
        email = request_data['email']

        if "@" in email and Authenticated_manager.objects.filter(email=email).exists():
            return JsonResponse(
                {
                    'email_error':
                    '&#x25cf; sorry email in use, choose another one'
                },
                status=409)
        elif "@" not in email:
            return JsonResponse(
                {
                    'email_error':
                    '&#x25cf; sorry, this is NOT a valid email address'
                },
                status=409)
        return JsonResponse({'email_valid': True}, status=200)


class SignUpUsernameValidationView(custom_view):
        # This checks the actual django auth model inside django for the username address returned by the request to establish it is unique

    def post(self, request):

        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse(
                {
                    'username_error':
                    '&#x25cf; username should only contain alphanumeric characters'
                },
                status=400)

        if Authenticated_manager.objects.filter(username=username).exists():
            return JsonResponse(
                {
                    'username_error':
                    '&#x25cf; sorry username in use, choose another one'
                },
                status=409)
        return JsonResponse({'username_valid': True}, status=200)


'''
These are the views for async validation of email !! DURING LOGIN !!
NOTE: The logic for the async validator for REGISTERATION is NOT the same
'''


class LoginEmailValidationView(custom_view):
        # This checks the actual django auth model inside django for the email address returned by the request actually exists

    def post(self, request):
        request_data = json.loads(request.body)
        email = request_data['email']

        if "@" in email and Authenticated_manager.objects.filter(email=email).exists():
            return JsonResponse(
                {
                    'email_valid': True
                },
                status=200)
        elif "@" not in email:
            return JsonResponse(
                {
                    'email_error':
                    '&#x25cf; sorry, this is NOT a valid email address'
                },
                status=409)

        return JsonResponse(
            {
                'email_error':
                '&#x25cf; sorry this email does NOT exist'
            },
            status=409)


class ActivateAccountView(custom_view):
    template_name = join_path(
        'Auth_templates', 'Account_confirmation', 'confirmed-account-login.html')
    invalid_activation_link = join_path(
        'Auth_templates', 'Account_confirmation', 'invalid-activation-link.html')

    def get(self, request, user_id, token):
        form_class = forms.LoginForm()
        try:
            user_id = force_text(urlsafe_base64_decode(user_id))
            user = Authenticated_manager.objects.get(pk=user_id)
        except(TypeError, ValueError, OverflowError, Authenticated_manager.DoesNotExist):
            user = None

        context = {
            'form': form_class,
            'today': Todays_Date,
            'panel_name': panel_name,
            'activation_message': 'Registration confirmation error . Please click the reset password to generate a new confirmation email.'
        }

        if user is not None and account_activation_token.check_token(user, token):
            # activate user and login [ login part commented out ]:
            user.is_active = True
            user.save()

            # login(request, user)
            # form = PasswordChangeForm(request.user)

            context['activation_message'] = 'Registration successful. Please login'

            return render(request, self.template_name, context=context)
        else:
            return render(request, self.invalid_activation_link, context=context)
            # return render(request, join_path('CoinEnvoy', 'Account_confirmation', 'invalid-activation-link.html'))

    def post(self, request):

        form_class = forms.LoginForm(request.user, request.POST)

        # Change password to usable one here [ see:

        # '''
        # user = form_class.save(commit=False)
        # user.is_active = False
        # # user.set_unusable_password()
        # user.save()

        # from UserRegisterView class above.
        # '''
        # ]

        # form_class = PasswordChangeForm(request.user, request.POST)

        if form_class.is_valid():
            context = {
                'form': form_class,
                'panel_name': panel_name,
            }
            user = form_class.save()
            # Important, to update the session with the new password
            update_session_auth_hash(request, user)
        return render(request, self.template_name, context=context)


class RegisterView(custom_view):
    template_name = join_path("Auth_templates", "register.html")
    email_sent_template = join_path(
        "Auth_templates", "Account_confirmation", "email-sent.html")

    def get(self, request):
        form = forms.RegisterationForm()
        # profile_form = forms.UserProfileForm()

        context = {
            "form": form,
            "today": Todays_Date,
            "panel_name": panel_name,
            # "profile_form": profile_form,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        form = forms.RegisterationForm(request.POST)
        # profile_form = forms.UserProfileForm(request.POST)

        context = {
            "form": form,
            "today": Todays_Date,
            "panel_name": panel_name,
            # "profile_form": profile_form,
        }

        try:
            # if form.is_valid() and profile_form.is_valid():
            if form.is_valid():
                new_manager = form.save(commit=False)
                # Old habits die hard. In newer django, you do not need to declear this
                #-----------------------------
                # "is_active" is a model field inside the main django model
                new_manager.is_active = True
                #-----------------------------
                new_manager.save()

                # new_manager_profile = profile_form.save(commit=False)
                # new_manager_profile.user = new_manager
                # new_manager_profile.save()

                # You can add some logic here to send email to the surveyor(s)

                # if EmailManager(request) == "email-sent":
                # return render(request, self.email_sent_template, context=context)
                messages.success(request, "Registeration Successful!!")
                return redirect(reverse("LoginView"))
                # return redirect(reverse("LoginView", args={"signup-success"}))
        except Exception as Error:
            raise Error

        return render(request, self.template_name, context=context)


class LoginView(custom_view):
    template_name = join_path("Auth_templates", "login.html")

    def get(self, request):
        form_class = forms.LoginForm()

        context = {
            "form": form_class,
            "today": Todays_Date,
            "panel_name": panel_name,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form_class = forms.LoginForm(request.POST)

        context = {
            "form": form_class,
            "today": Todays_Date,
            "panel_name": panel_name,
        }

        pprint(form_class)

        if form_class.is_valid():
            form_instance = form_class.save(commit=False)
            # form_instance.save()
            username = Authenticated_manager.objects.get(
                email=form_instance.email.lower()).username

            print(username)

            user = authenticate(
                request,
                username=username.strip(),
                password=form_instance.password,
            )

            pprint(user)

            if user is None:
                context = {
                    # "login_error": "Login was unsuccessful, Please try again.",
                    "form": form_class,
                    "today": Todays_Date,
                }
                print("User is not logged in")
                message.error(
                    request, "Login was unsuccessful, Please try again.")
                return render(request, self.template_name, context)
            else:
                login(request, user)
                pprint(request.POST)

            if request.user.is_authenticated:
                try:
                    return redirect("PrimeAccessView")
                except Exception as Error:
                    raise Error
        else:
            pprint(form_class.errors)
            print("\n" "form is invalid")
            return render(request, self.template_name, context)

        return render(request, self.template_name, context)

# Do a logout page


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):

    args = {
        "today": Todays_Date,
        "panel_name": panel_name,
    }
    extra_conext = args
    next_page = reverse_lazy('LoginView')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS,
                             "You are now logged out !!")
        return response
