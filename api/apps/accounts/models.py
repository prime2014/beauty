from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone



class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        password=None,
        is_active=False,
        is_staff=False,
        is_superuser=False,
        **extra_fields):
        user = self.model(email=email, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)

        if password:
            user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_kwargs):
        return self.create_user(email, password, is_active=True, is_staff=True, is_superuser=True, **extra_kwargs)

    def is_staff(self):
        return self.is_staff


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=40)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
        default=timezone.now,
        editable=False
    )

    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser or self.is_active

    def has_module_perms(self, app_label):
        return self.is_superuser
