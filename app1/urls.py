# app1/urls.py
from django.urls import path
from app1.views.patient_views import patient_view
from app1.views.register_view import register
from app1.views.log_in_view import login_view
from app1.views.welcome_view import welcome
from app1.views.logout_views import logout_view
from app1.views.profile_view import profile_view
from app1.views.home_view import home
from app1.views.email_send import CustomPasswordResetView
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenRefreshView
from  app1.views.log_api import LoginView
from app1.views .register_api import register_api
from app1.views.password_reset_apii_view import PasswordResetRequestAPIView
from app1.views.confirm_password_reset_view import PasswordResetConfirmAPIView
urlpatterns = [
    path('patient/', patient_view, name="patient_list"),
    path('reg/', register, name="register"),
    path('login/', login_view, name="login"),
    path('welcome', welcome, name="welcome"),
    path('logout', logout_view, name='logout'),
    path('profile', profile_view, name='profile'),
    path('', home, name="front"),
    path('api_login/',LoginView.as_view(),name='api_loin'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api_register/', register_api, name='api-register'),
    path('api_password_reset/', PasswordResetRequestAPIView.as_view(), name='password_reset_api'),
    path('api_reset/<uidb64>/<token>/', PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm_api'),

    # Password Reset URLs
    path('password_reset/', CustomPasswordResetView.as_view(template_name="registration/password_reset.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
    
]
