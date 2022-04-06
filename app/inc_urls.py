from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ask/', views.ask),
    path('<int:i>/', views.question, name="question")
]