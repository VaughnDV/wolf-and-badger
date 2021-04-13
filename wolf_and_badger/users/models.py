from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, DateTimeField, ManyToManyField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField


class Address(Model):
    street_address = CharField(max_length=256, null=False)
    area = CharField(max_length=128, null=True, blank=True)
    post_code = CharField(max_length=24, null=False)
    country = CharField(max_length=128, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.street_address


class User(AbstractUser):
    """Default user for Wolf and Badger."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    addresses = ManyToManyField(Address, null=True, blank=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
