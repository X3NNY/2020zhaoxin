"""recruit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from chall import urls as chall_urls
from . import views as views
from captcha import urls as captcha_urls

urlpatterns = [
    path('',views.index),
    path('nimda/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.loginPage),
    path('register/', views.registerPage),
    path('api/user/login',views.login),
    path('api/user/register',views.register),
    path('api/user/logout',views.logout),
    path('chall/',include(chall_urls)),
    path('user/',views.me),
    path('captcha/',include(captcha_urls)),
    path('signup/', views.gameSignUp)

]
