# app1/urls.py
from django.urls import path
from app1.views.patient_views import patient_view
from app1.views.register_view import register
from app1.views.log_in_view import login_view
from app1.views.welcome_view import welcome
from app1.views.logout_views import logout_view
from app1.views.profile_view import profile_view
from app1.views.home_view import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('patient/', patient_view, name="patient_list"),
    path('reg/', register, name="register"),
    path('login/', login_view, name="login"),
    path('welcome', welcome, name="welcome"),
    path('logout', logout_view, name='logout'),
    path('profile', profile_view, name='profile'),
    path('', home, name="front"),

    # Password Reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
]
