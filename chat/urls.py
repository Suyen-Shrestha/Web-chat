from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.startpage, name="start-page"),
    path('signup/', views.signup, name="signup"),
    path('login/', LoginView.as_view(template_name='chat/login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]