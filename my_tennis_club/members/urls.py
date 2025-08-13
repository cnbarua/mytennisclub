from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.members, name='members'),
    path('members/details/<slug:slug>/', views.details, name='details'),
    # Add the testing, contact path
    path('testing/', views.testing, name='testing'),
    path('contact/', views.contact, name='contact'),
    path('react/', views.react, name='react'),
]
