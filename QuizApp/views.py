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

def admin_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('admin_login')

from django.contrib.auth.decorators import user_passes_test

def is_staff_user(user):
    return user.is_authenticated and user.is_staff

from .models import AISettings
@user_passes_test(is_staff_user, login_url='admin_login')
def ai_settings(request):
    ai_settings = AISettings.get_solo()
    if request.method == 'POST':
        gemini_api_key = request.POST.get('gemini_api_key', '')
        gemini_model = request.POST.get('gemini_model', 'gemini-2.5-flash')
        ai_settings.gemini_api_key = gemini_api_key
        ai_settings.gemini_model = gemini_model
        ai_settings.save()
        messages.success(request, 'AI settings updated successfully!')
        return redirect('ai_settings')

    return render(request, 'ai_settings.html', {'current_model': ai_settings})



