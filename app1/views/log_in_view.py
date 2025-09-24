from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from app1.forms.login_form import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')  # Redirect to your home/dashboard page
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'login.html', {'form': form})
