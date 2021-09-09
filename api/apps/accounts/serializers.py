from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password


User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "email",
            "password"
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "email",
            "first_name",
            "last_name",
            "password",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined"
        )

        extra_kwargs = {
            "password": {"write_only": True},
            "is_staff": {"write_only": True},
            "is_superuser": {"write_only": True}
        }

    def create(self, validated_data):
        if validated_data.get("is_active"):
            validated_data["is_active"] = False
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        instance.password = validated_data.get("password", instance.password)
        instance.password = make_password(instance.password)
        instance.save()
        return instance
