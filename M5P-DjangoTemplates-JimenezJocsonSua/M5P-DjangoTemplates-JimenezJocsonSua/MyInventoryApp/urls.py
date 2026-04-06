"""
URL configuration for MyInventorySystem project.
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'), # This makes localhost:8000/ load the login page
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('manage_account/<int:pk>/', views.manage_account_view, name='manage_account'),
    path('change_password/<int:pk>/', views.change_password_view, name='change_password'),
    path('delete_account/<int:pk>/', views.delete_account_view, name='delete_account'),

    path('view_supplier/', views.view_supplier, name='view_supplier'),
    path('view_bottles/', views.view_bottles, name='view_bottles'),
    path('add_bottle/', views.add_bottle, name='add_bottle'),
    
    path('view_bottle_details/<int:pk>/', views.view_bottle_details, name='view_bottle_details'),
]