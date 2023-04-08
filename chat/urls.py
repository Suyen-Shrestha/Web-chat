from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.startpage, name="start-page"),
    path('signup/', views.signup, name="signup"),
    path('login/', LogoutView.as_view(), name="logout"),
]