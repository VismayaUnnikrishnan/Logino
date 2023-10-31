from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('profile', profile, name='profile'),

    path('password_change/', password_change, name='password_change'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/changed.html'), name='password_change_done'),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
