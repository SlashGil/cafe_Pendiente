from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from coffee.variables.ModelsConstants import MAX_LENGTH_USER_NAME, MAX_LENGTH_PASSWORD


# Create your models here.

def is_valid_date_time(new_time, saved_time):
    minus = new_time - saved_time
    operation = minus.total_seconds() / 3600
    return operation >= 8


class Coffee(models.Model):
    username = models.TextField(max_length=MAX_LENGTH_USER_NAME)
    giftTo = models.TextField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "coffee"

    def can_be_gifted(self, coffee_to_gift):
        giftTo = coffee_to_gift.giftTo
        time = coffee_to_gift.time
        coffee = Coffee.objects.filter(giftTo=coffee_to_gift.giftTo).order_by('time').first()
        if coffee is not None:
            return is_valid_date_time(time, coffee.time)
        else:
            return True
