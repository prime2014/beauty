from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, authentication, status
from django.contrib.auth import get_user_model
from apps.accounts.serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.accounts.auth import Authentication
from django.contrib.auth import login


authentication = Authentication().authenticate


User = get_user_model()


class LoginViewset(APIView):
    authentication_classes = ()
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authentication(request, username=email, password=password)
        if user:
            login(request, user)
            return Response({"token": user.auth_token.key, "user": UserSerializer(instance=user).data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid User Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
