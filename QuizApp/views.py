from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user) # log the user in
            messages.success(request, 'Successfully logged in as admin.')
            return redirect('ai_settings')

        messages.error(request, "Invalid credentials or not an admin user.")
        return redirect('admin_login') # redirect back to login or failure
    return render(request, 'admin_login.html')

