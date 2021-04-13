from django.urls import path

from wolf_and_badger.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    create_address_view,
)

app_name = "users"
urlpatterns = [
    path("create_address/", view=create_address_view, name="create_address"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
