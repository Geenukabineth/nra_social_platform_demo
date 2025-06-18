from django.shortcuts import render


def login_view(request):
    return render(request, 'page/Login.html')



def landing (request):
    return render (request, "page/landing.html")


def userSingup (request):
    return render (request, "page/Register.html")