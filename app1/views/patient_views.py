from django.shortcuts import render
from app1.models.patient_models import patient


def patient_view(request):
    patients=patient.objects.all()
    return render(request,'patient_list.html',{"patients":patients})
