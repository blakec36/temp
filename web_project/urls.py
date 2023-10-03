"""
URL configuration for web_project project.

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
from django.urls import include, path
from dashboard import views

urlpatterns = [
    path("", views.home),
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('kauai/', views.kauai),
    path('catalina/', views.catalina),
    path('mutau/', views.mutau),
    path('canada/', views.canada),
    path('ireland/', views.ireland),
    path('poland/', views.poland),
    path('golf/', views.golf),
    path('upcoming/', views.upcoming),
]