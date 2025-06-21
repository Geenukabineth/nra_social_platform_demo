from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.urls import reverse
from django.contrib import messages
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser or user.is_staff:
                return HttpResponseRedirect(reverse("adminview"))  
            else:
                return render(request, "base.html", {"data": user})
        else:
            return render(request, "page/login.html", {"error": "Invalid username or password"})
    else:
        return render(request, "page/login.html")


def landing(request): 
    return render(request, "page/landing.html")


def logout_view(request):
    logout(request)
    return redirect("landing")  


@login_required
def base(request):
    return render(request, "base.html")


@login_required
def adminview(request):  
    return render(request, "admin.html")


@csrf_exempt
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password2")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect(request, "page/Register.html")

        try:
            user = User.objects.create_user(username=username, email=email, password=password)  
            messages.success(request, "Account created successfully!")
            return redirect("login")

        except Exception as e:

            messages.error(request, f"An error occurred during signup: {str(e)}")
            return redirect("login")
    else:
        return render(request, "page/Register.html")


def create_product(request):  
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully!")
            return redirect("adminview")  
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProductForm()

    return render(request, "components/Product.html", {"form": form})


def create_event(request):  
    if request.method == "POST":
        form = EventForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Event created successfully!")
            return redirect("adminview")  
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EventForm()

    return render(request, "page/Event.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("landing")


def product_list(request):
    products = Product.objects.all()
    return render(request, "base.html", {"products": products})


def event_list(request):
    events = Event.objects.all()
    return render(request, "base.html", {"events": events})


def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Event created successfully!")
            return redirect("admin")  
    else:
        form = EventForm()

    return render(request, "page/Event.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("landing")  




def user_data(request):
    data = User.objects.all()
    return render(request, "base.html", {"data": data})