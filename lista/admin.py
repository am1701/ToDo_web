from django.contrib import admin
from .models import Lista, User
from django.contrib.auth import admin as auth_adim

admin.site.register(User, auth_adim.UserAdmin)

admin.site.register(Lista)
# Register your models here.
