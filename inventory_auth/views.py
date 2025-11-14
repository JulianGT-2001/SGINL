from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login_view(request):
    if (request.method == "POST"):
        usuario = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=usuario, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login exitoso')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'inventory_auth/login.html')