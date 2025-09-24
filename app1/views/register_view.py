from app1.forms.register_form import RegisterForm
from app1.models.patient_models import patient
from django.shortcuts import render,redirect

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            patient.objects.create(user=user, age=form.cleaned_data['age'], disease="")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})
