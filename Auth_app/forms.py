from django import forms
from django.apps import apps
from .models import UserProfile
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import (
    UserCreationForm, 
    AuthenticationForm,
)

# GET Authenticated user model.
# -----------------------------
Authenticated_manager = get_user_model()


class RegisterationForm(UserCreationForm):

    username = forms.CharField(
        label='User Name',
        widget=forms.TextInput(
            attrs={

                'type': 'text',
                'id': 'yourUsername',
                'name': 'username',
                'placeholder': '',
                # 'required': 'required',
                'class': 'form-control',
            }
        )
    )

    email = forms.CharField(
        label='Email Address',
        widget=forms.EmailInput(
            attrs={

                'type': 'email',
                'id': 'yourEmail',
                'name': 'email',
                'placeholder': '',
                'class': 'form-control',

            }
        )
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={

                'type': 'password',
                'name': 'password1',
                'id': 'yourPassword1',
                'class': 'form-control',

            }
        )
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={

                'type': 'password',
                'name': 'password2',
                'id': 'yourPassword2',
                'class': 'form-control',

            }
        )
    )

    class Meta:
        model = Authenticated_manager
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

        exclude = (
            'first_name',
            'last_name',
        )

    def clean_email(self):
        useremail = self.cleaned_data['email'].lower()
        Authenticated_Manager = Authenticated_manager.objects.filter(email=useremail)
        if Authenticated_Manager.exists():
            raise ValidationError(
                f'This user email: "{useremail}" is already in use !!')
        return useremail

    def save(self, commit=True):
        Authenticated_Manager = super(RegisterationForm, self).save(commit=False)
        Authenticated_Manager.username = self.cleaned_data['username']
        Authenticated_Manager.email = self.cleaned_data['email']

        if commit:
            Authenticated_Manager.save()

        return Authenticated_Manager


class UserProfileForm(forms.ModelForm):
    ''' NOTE!!!: Do not touch this class for an reason. The text input tyoes are there because
    postgres db has a problem with normal integer field which take long digits eg phonenumbers, I don't know why. '''

    userphonenumber = forms.CharField(
        label='Phone Number',
        widget=forms.NumberInput(
            attrs={

                'type': 'text',
                'id': 'userphone',
                'maxlength': '20',
                'name': 'userphonenumber',
                'placeholder': 'Phone Number',
                'class': 'form-control',

            }
        )
    )

    class Meta:
        model = UserProfile
        fields = (
            'userphonenumber',
        )

    # You must use the exact name of the field in the form here or the function wont't run.
    def clean_userphonenumber(self):
        phonenumber = self.cleaned_data['userphonenumber']
        Auth_user = UserProfile.objects.filter(
            userphonenumber=phonenumber
        )
        try:
            if int(phonenumber) and not str(phonenumber):
                min_length = 10
                max_length = 13
                ph_length = str(phonenumber)
                if len(ph_length) < min_length or len(ph_length) > max_length:
                    raise ValidationError('Phone number length not valid')

            if Auth_user.exists():
                raise ValidationError(
                    f'This user phone number: "{phonenumber}" is already in use !!')

        except (ValueError, TypeError):
            raise ValidationError('Please enter a valid phone number')

        return phonenumber

    def save(self, commit=True):
        UserProfile = super(UserProfileForm, self).save(commit=False)
        try:
            UserProfile.userphonenumber = self.cleaned_data['userphonenumber']
        except Exception as Error:
            raise (Error)

        if commit:
            try:
                UserProfile.save()
            except Exception as Error:
                raise (Error)

        return UserProfile



class LoginForm(forms.ModelForm):
    # uncomment email and comment username

    email = forms.CharField(
        label='Email Address',
        widget=forms.EmailInput(
            attrs={

                'type': 'email',
                'id': 'yourEmail',
                'name': 'email',
                'placeholder': '',
                'required': 'required',
                'class': 'form-control',

            }
        )
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={

                'id': 'password3',
                'type': 'password',
                'name': 'password',
                'placeholder': '',
                'class': 'form-control',
            }
        )
    )

    # remember_me = forms.BooleanField(
    #     required=False,
    #     label='Remember Me',
    #     widget=forms.CheckboxInput(
    #         attrs={

    #             'type': 'checkbox',
    #             'id': 'remember_me',
    #             'checked': 'checked',
    #             'name': 'remember_me',
    #             'class': 'form-control form-control-lg',
    #         }
    #     )
    # )

    class Meta:
        model = Authenticated_manager

        fields = (
            'email',
            'password',
        )

        exclude = (
            'first_name',
            'last_name',
            'username',
        )
