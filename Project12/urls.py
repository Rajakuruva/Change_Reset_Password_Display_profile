"""
URL configuration for Project12 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Registartion/',Registartion,name='Registartion'),
    path('Home/',Home,name='Home'),
    path('User_login/',User_login,name='User_login'),
    path('Log_out/',Log_out,name='Log_out'),
    path('Display_Profile/',Display_Profile,name='Display_Profile'),
    path('Change_password/',Change_password,name='Change_password'),
    path('Forgot_Password/',Forgot_Password,name='Forgot_Password'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)