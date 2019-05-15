from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, UserProfile


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'full_name', 'user_role', 'phone_no')



class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'phone_no', 'user_role')


class CustomUserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('avatar',)
