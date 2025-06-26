from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username",'first_name', "last_name","email",'password1','password2']


    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Please enter the same password")

        validate_password(password2)
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = self.cleaned_data["password1"]
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description",'start_date', 'end_date',"location"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Event Title"}),
            "description": forms.Textarea(attrs={"class": "form-label", "placeholder": "Event Description"}),
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "location": forms.TextInput(attrs={"class": "form-control", "placeholder": "Event Location"}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'required': True}),
            'price': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01', 'required': True}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Enter product description...'}),
            'image': forms.FileInput(attrs={'class': 'form-file', 'accept': 'image/*'}),
        }



