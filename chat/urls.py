from django.contrib import admin
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.startpage, name="start-page"),
    path('signup/', views.signup, name="signup"),
]