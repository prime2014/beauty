from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication, permissions, status, exceptions
from apps.blog.models import Blog
from apps.blog.serializers import BlogSerializer
from rest_framework.response import Response


class BlogViewset(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
