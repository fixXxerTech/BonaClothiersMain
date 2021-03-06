from django.db import models
from django.contrib.auth import get_user_model


# GET Authenticated user model.
# -----------------------------
Authenticated_manager = get_user_model()


class UserProfile(models.Model):

    user = models.OneToOneField(
        Authenticated_manager,
        max_length=300,
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='surveyor',  # related name manager if needed
        null=False,
        blank=False,
    )

    userphonenumber = models.CharField(
        help_text='Your phone number',
        max_length=20,
        unique=True,
        blank=True,
        null=True,
    )

    useraddress = models.CharField(
        help_text='Your address',
        max_length=20,
        unique=True,
        blank=True,
        null=True,
    )

    def __str__(self):
        return '{}, manager profile.'.format(self.user.username)
