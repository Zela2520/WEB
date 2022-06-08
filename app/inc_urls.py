from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ask/', views.ask, name="ask"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
    path('settings/', views.settings, name="settings"),
    path('hot/', views.hot, name="hot_question"),
    path('tag/', views.tag_listing, name="tag_listing"),
    path('<int:i>/', views.question, name="question")
]