from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, CreateView, DeleteView
from .models import Address
from .forms import CreateAddressForm

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["name", "phone_number", "addresses"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.request.user.get_absolute_url()  # type: ignore [union-attr]

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class CreateAddressView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Address
    login_url = '/login/'
    redirect_field_name = "users:detail"
    form_class = CreateAddressForm
    success_message = _("Address successfully created")

    def get_success_url(self):
        return self.request.user.get_absolute_url()


create_address_view = CreateAddressView.as_view()


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    success_url = redirect_field_name = "home"
    success_message = _("Account successfully deleted")


user_delete_view = UserDeleteView.as_view()
