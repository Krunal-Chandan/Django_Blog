from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        help_text="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unique Username'})
    )
    email = forms.EmailField(
        help_text="",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Office Email'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        help_text=""
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        help_text=""
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        help_text="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unique Username'})
    )
    email = forms.EmailField(
        help_text="",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Office Email'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
        }