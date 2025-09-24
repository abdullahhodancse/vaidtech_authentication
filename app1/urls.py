from django.urls import path
from app1.views.patient_views import patient_view
from app1.views.register_view import register
from app1.views.lon_in_view import login_view
from app1.views.welcomw_view import welcome
from app1.views.logout_views import logout_view

urlpatterns=[
    path('patient/',patient_view,name="patient_list"),
    path('reg/',register,name="register"),
    path('login/',login_view,name="login"),
    path('welcome',welcome,name="welcome"),
    path('logout',logout_view,name='logout')
]