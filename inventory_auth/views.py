from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def login_view(request):
    # Si el usuario ya está autenticado, redirigir al dashboard
    if request.user.is_authenticated:
        return redirect('inventory:dashboard')
    
    if (request.method == "POST"):
        usuario = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=usuario, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login exitoso')
            return redirect('inventory:dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'inventory_auth/login.html')

@login_required(login_url='inventory_auth:login')
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente')
    return redirect('inventory_auth:login')