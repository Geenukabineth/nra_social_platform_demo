from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser or user.is_staff:
                return Response(reverse("base"))
            else:
                return render(request, "index.html", {"data": user})
        else:
            return render(request, "page/login.html", {"error": "Invalid username or password"})
    else:
        return render(request, "page/login.html")


def landing (request):
    return render (request, "page/landing.html")


def userSingup (request):
    return render (request, "page/Register.html")


def base(request):
    return render(request, "base.html")


@api_view(["POST"])
@permission_classes([AllowAny])
@csrf_exempt
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password2")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "registration/signup.html", {"error": "Username already exists"})

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created successfully!")
            return redirect("login")

        except Exception as e:
            messages.error(request, f"An error occurred during signup: {str(e)}")
            return render(request, "registration/signup.html", {"error": f"An error occurred during signup: {str(e)}"})
    else:
        return render(request, "registration/signup.html")
