from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile, Snippet

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = [
            'title',
            'language',
            'category',
            'description',
            'code',
            'public',
        ]


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'avatar',
        ]