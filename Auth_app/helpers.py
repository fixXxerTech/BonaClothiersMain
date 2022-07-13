from os.path import join as join_path

from django.conf import settings
# from django.utils import timezone
from django.contrib import messages
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.auth import update_session_auth_hash
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import get_template, render_to_string


def EmailManager(request):

    prefix = 'https://'

    Host_name = get_current_site(request)
    Host_name = str(Host_name.domain)

    # form_class = forms.RegisterationForm(request.POST)
    # profile_form_class = forms.UserProfileForm(request.POST)

    # context = {
    #     'form': form_class,
    #     'profile_form': profile_form_class,
    #     'message': 'You are registered successfully !!',
    # }

    try:
        # if form_class.is_valid() and profile_form_class.is_valid():
        #     # Create an inactive user with no password:

        #     user = form_class.save(commit=False)
        #     user.is_active = False
        #     # user.set_unusable_password()
        #     user.save()

        #     # user profile save with user instance assigned.
        #     profile_form = profile_form_class.save(commit=False)
        #     profile_form.user = user
        #     profile_form.save()

        #     username = form_class.cleaned_data.get('username')
        #     raw_password = form_class.cleaned_data.get('password2')

        #     messages.success(request, f'Account created for {username}!')

        # Send an email to the user with the token:
        user = request.user
        token = account_activation_token.make_token(user)
        user_id = urlsafe_base64_encode(force_bytes(user.id))

        url = prefix + Host_name + \
            reverse('activate', kwargs={
                    'user_id': user_id, 'token': token})

        subject = 'Fashion App Account Verification'
        message = render_to_string(
            join_path('Auth_templates', 'Account_confirmation', 'account-activation-email.html'), {
                'confirm_url': url,
                'username': user.username,

                'activation_link': Host_name,
                'coin_envoy_logo': join_path(Host_name, 'static', 'img', 'logo-primary.png'),
                'coin_envoy_email_image': join_path(Host_name, 'static', 'img', 'email-opened.svg'),
                'coin_envoy_email_background': join_path(Host_name, 'static', 'img', 'body-bg.png'),
            })

        # One way to send the email is by using the simple email_user(subject, message) function in the
        # user instance by default

        # E.g: user.email_user(subject, message)

        # But I prefer EmailMessage class as seen below.

        # message = get_template('account_activation_email.html').render({
        #   'confirm_url': url,

        # })

        confirmation_mail = EmailMessage(
            subject,
            message,
            to=[user.email],
            from_email=settings.EMAIL_HOST_USER,
        )

        confirmation_mail.content_subtype = 'html'
        confirmation_mail.send()

        return 'email-sent'

    except Exception as Error:
        raise Error

        # return render(request, join_path('Auth_templates', 'Account_confirmation', 'email-sent.html'), context)
