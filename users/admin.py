from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, Profile

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     list_display = ["email", 'username', 'cat']
#     model = CustomUser

admin.site.register(CustomUser)
admin.site.register(Profile)
