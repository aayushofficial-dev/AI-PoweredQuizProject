from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='quiz_home'),
    path('about/', about, name='quiz_about'),
    path('admin_login/', admin_login, name='admin_login'),
    path('admin_logout/', admin_logout, name='admin_logout'),
    path('ai_settings/', ai_settings, name='ai_settings'),
]