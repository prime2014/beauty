from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/users/", include("rest_framework.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("blogs/", include("apps.blog.urls"))
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls))
    ]+urlpatterns
