from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="To‘g‘ri email manzilini kiriting.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Bu email allaqachon ro‘yxatdan o‘tgan. Boshqasini kiriting.")
        return email

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, help_text="To‘g‘ri email manzilini kiriting.")
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )