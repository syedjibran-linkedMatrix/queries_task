from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Nurse(models.Model):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    doctor = models.ManyToManyField(Doctor, related_name='patients')
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='patients')
    date_admitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='hospitals')
    doctor = models.ManyToManyField(Doctor)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)

    def __str__(self):
        return f"Hospital record for {self.patient.name}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    diagnoses = models.TextField()
    prescription = models.TextField()

    def __str__(self):
        return f"Medical record for {self.patient.name}"
