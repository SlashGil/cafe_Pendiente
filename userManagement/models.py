from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

from coffee.variables.ModelsConstants import MAX_LENGTH_USER_NAME, MAX_LENGTH_PASSWORD


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener email')
        if password:
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        else:
            raise ValueError('El usuario debe tener contraseña')

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super usuario debe tener is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super usuario debe tener is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(max_length=MAX_LENGTH_USER_NAME, unique=True)
    name = models.TextField(max_length=MAX_LENGTH_USER_NAME)
    username = models.CharField(max_length=MAX_LENGTH_USER_NAME)
    password = models.TextField(max_length=MAX_LENGTH_PASSWORD)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "password", "username"]

    objects = UserManager()

    def __str__(self):
        return self.name
