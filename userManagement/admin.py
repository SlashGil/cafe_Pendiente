from django.contrib import admin

from coffee.models import Coffee
from userManagement.models import User

# Register your models here.
admin.site.register(Coffee)
admin.site.register(User)