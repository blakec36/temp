from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
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
