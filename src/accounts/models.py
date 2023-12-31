from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    A `CustomUser` so we can add our own functionality for site users.
    """

    # `registration_accepted` is used to control access to the site.
    registration_accepted = models.BooleanField(
        verbose_name="Registration Accepted",
        help_text=(
            "Designates whether this user's registration has been accepted."
        ),
        default=False,
    )

    def __str__(self):
        """
        String representation of CustomUser.
        """
        return self.username
