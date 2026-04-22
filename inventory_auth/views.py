from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def login_view(request):
    # Si el usuario ya está autenticado, redirigir
    if request.user.is_authenticated:
        next_url = request.GET.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('inventory:dashboard')
    
    if (request.method == "POST"):
        usuario = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=usuario, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login exitoso')
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('inventory:dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    next_url = request.GET.get('next', '')
    return render(request, 'inventory_auth/login.html', {'next': next_url})

@login_required(login_url='inventory_auth:login')
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente')
    return redirect('inventory_auth:login')