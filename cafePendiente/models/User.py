from django.db import models

from cafePendiente.variables.ModelsConstants import MAX_LENGTH_USER_NAME, MAX_LENGTH_PASSWORD


class User(models.Model):
    Name = models.CharField(max_length=MAX_LENGTH_USER_NAME)
    UserName = models.CharField(max_length=MAX_LENGTH_USER_NAME)
    Password = models.CharField(max_length=MAX_LENGTH_PASSWORD)

