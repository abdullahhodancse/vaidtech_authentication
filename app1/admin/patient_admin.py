from django.contrib import admin
from app1.models.patient_models import patient

@admin.register(patient)

class Patientadmin(admin.ModelAdmin):
    list_display=('user','age','disease')
    search_fields=('user__first_name','user__last_name','disease','user__email')
    list_filter=('age','disease','user__is_active','user__is_staff')
    ordering=('age',)
    list_editable=('age','disease')




