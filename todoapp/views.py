from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.
@login_required
def home(request):
    todos = Task.objects.filter(user=request.user)
    return render(request, "index.html", {"todos": todos})

def register_view(request):
    if request.method == "POST":
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password_input != confirm_password:
            return render(request, "register.html", {"error": "Password tidak cocok!"})
            
        if User.objects.filter(username=username_input).exists():
            return render(request, "register.html", {"error": "Username sudah digunakan!"})
            
        User.objects.create_user(username=username_input, password=password_input)
        
        return redirect('login')
        
    return render(request, "register.html")

def login_view(request):
    if request.method == 'POST':
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')

        user = authenticate(request, username=username_input, password=password_input)
        
        if user is not None:
            login(request, user)  
            return redirect('home')  
        else:
            return render(request, "login.html", {"error": "Username atau password salah!"}) 

    return render(request, "login.html")

# 4. HALAMAN LOGOUT
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def delete_task(request, id):
    return redirect('home')

@login_required
def add_todo(request):
    if request.method == "POST":
        title_input = request.POST.get('title')
        if title_input: 
            Task.objects.create(
                user=request.user,
                title=title_input
            )
        return redirect('home')
    return redirect('home')