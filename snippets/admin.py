from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Snippet, Category, Profile

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Snippet)
admin.site.register(Category)
admin.site.register(models.Profile)