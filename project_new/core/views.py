from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser or user.is_staff:

                return redirect("adminview")

            else:
                return render(request, "base.html", {"data": user})
        else:
            return render(request, "page/login.html", {"error": "Invalid username or password"})
    else:
        return render(request, "page/login.html")


def landing(request): 
    return render(request, "page/landing.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect("landing")  


@login_required
def dashboard_view(request):
    products = Product.objects.all()
    events = Event.objects.all()  

    context = {  
        "products": products,
        "events": events,
        "data": request.user,  
    }

    return render(request, "base.html", context)


@login_required
def admin_panel_view(request):
    total_users = User.objects.count()
    total_products = Product.objects.count()
    total_events = Event.objects.count()

    context = {
        "total_users": total_users,
        "total_products": total_products,
        "total_events": total_events,
        "total_revenue": 0,
        "recent_activities": [],
        "users": {"count": total_users},
        "products": {"count": total_products},
        "total_events": {"count": total_events},
        "data": request.user,
    }

    return render(request, "admin.html", context)


@csrf_exempt
def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password_confirm = request.POST.get("password2")

        if not all([first_name, last_name, username, email, password]):
            messages.error(request, "All fields are required")
            return redirect('/register/')

        if password != password_confirm:
            messages.error(request, "Passwords don't match")
            return redirect('/register/')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
            return redirect('/register/')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
            return redirect('/register/')

        try:
            validate_password(password)
        except ValidationError as e:
            messages.error(request, ' '.join(e.messages))
            return redirect('/register/')

        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)  
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('/login/')

    return render(request, 'page/Register.html')


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            
            form.save()
            messages.success(request, "Product created successfully!")
            return redirect("adminview")
        else:
            print("Form errors:", form.errors)  
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

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("landing")

def user_data(request):
    users = User.objects.all()
    return render(request, "admin.html", {"data": users})



