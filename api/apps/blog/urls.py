from rest_framework.routers import DefaultRouter
from django.urls import path, include
from apps.blog.api import BlogViewset

router = DefaultRouter()

router.register(r"blogs", viewset=BlogViewset, basename="blogs")


urlpatterns = [
    path("api/v1/", include(router.urls))
]
