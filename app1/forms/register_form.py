
from django import forms
from django.contrib.auth import get_user_model
from app1.models.custome_user import User



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.IntegerField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
