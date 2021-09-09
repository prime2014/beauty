from rest_framework.routers import DefaultRouter
from django.urls import path, include
from apps.accounts.api import UserViewset, LoginViewset

app_name = "accounts"

router = DefaultRouter()

router.register(r"users", viewset=UserViewset, basename="users")


urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("login/", LoginViewset.as_view(), name="login")
]
