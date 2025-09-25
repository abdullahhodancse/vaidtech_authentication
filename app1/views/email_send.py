from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from app1.task import send_reset_email

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')

    
