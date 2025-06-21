from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django import forms 


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"})
    )
    terms = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
        }

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
        user.agreed_to_terms = self.cleaned_data["terms"]
        if commit:
            user.save()
        return user



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description",'start_date', 'end_date',"location"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Event Title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Event Description"}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            "location": forms.TextInput(attrs={"class": "form-control", "placeholder": "Event Location"}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-admin-primary focus:border-transparent'}),
            'price': forms.NumberInput(attrs={'class': 'p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-admin-primary focus:border-transparent', 'step': '0.01'}),
            'category': forms.Select(attrs={'class': 'p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-admin-primary focus:border-transparent'}),
            'description': forms.Textarea(attrs={'class': 'p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-admin-primary focus:border-transparent resize-vertical min-h-24'}),
            'image': forms.FileInput(attrs={'class': 'p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-admin-primary focus:border-transparent'}),
        }