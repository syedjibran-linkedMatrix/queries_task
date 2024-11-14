from django.contrib import admin
from .models import Doctor, Nurse, Patient, Hospital, MedicalRecord

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'date_admitted')  
    search_fields = ('name',)  
    list_filter = ('doctor',)  

admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Hospital)
admin.site.register(MedicalRecord)
