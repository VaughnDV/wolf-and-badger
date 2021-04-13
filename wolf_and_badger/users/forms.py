from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Address

User = get_user_model()


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return member.street_address


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User

    addresses = CustomMMCF(
        queryset=Address.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class CreateAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('street_address', 'area', 'post_code', 'country')
