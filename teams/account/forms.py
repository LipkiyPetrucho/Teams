from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, DateInput, EmailInput

from account.models import Profile


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ["username", "password"]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use.")
        return email


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": TextInput(
                attrs={
                    "class": "form-control mr-2",
                    "placeholder": "Имя пользователя",
                }
            ),
            "last_name": TextInput(
                attrs={
                    "class": "form-control mr-2",
                    "placeholder": "Фамилия пользователя",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control mr-2",
                    "placeholder": "Электронная почта",
                }
            ),
        }

    def clean_email(self):
        data = self.cleaned_data["email"]
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError("Email already in use.")
        return data


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth", "location"]
        widgets = {
            "date_of_birth": DateInput(
                attrs={
                    "class": "form-control mr-2",
                    "type": "date",
                    "placeholder": "Enter your birth date",
                    "name": "date_of_birth",
                    "id": "id_date_of_birth",
                }
            ),
            "location": TextInput(
                attrs={
                    "class": "form-control mr-2",
                    "placeholder": "Введите название города",
                    "name": "location",
                    "id": "id_location",
                    "autocomplete": "off",
                }
            ),
        }
