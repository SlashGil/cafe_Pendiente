from django.db import models

from cafePendiente.variables.ModelsConstants import MAX_LENGTH_USER_NAME


class Coffee(models.Model):
    User = models.CharField(max_length=MAX_LENGTH_USER_NAME)
    giftTo = models.CharField(max_length=MAX_LENGTH_USER_NAME)