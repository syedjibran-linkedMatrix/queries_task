import random
from django.core.management.base import BaseCommand
from faker import Faker
from myapp.models import Doctor, Nurse, Patient, Hospital, MedicalRecord

fake = Faker()

class Command(BaseCommand):
    help = 'Populates the database with fake data for Doctor, Nurse, Patient, Hospital, and MedicalRecord models'

    def handle(self, *args, **kwargs):
        # Create Doctors
        doctors = []
        for _ in range(50):  # Create 50 doctors
            doctor = Doctor.objects.create(
                name=fake.name(),
                specialization=fake.job(),
                contact_number=fake.phone_number()
            )
            doctors.append(doctor)
        self.stdout.write(self.style.SUCCESS('Created 50 doctors'))

        nurses = []
        for _ in range(50):  
            nurse = Nurse.objects.create(
                name=fake.name(),
                contact_number=fake.phone_number()
            )
            nurses.append(nurse)
        self.stdout.write(self.style.SUCCESS('Created 50 nurses'))

        patients = []
        for _ in range(50):  
            patient = Patient.objects.create(
                name=fake.name(),
                age=random.randint(18, 100),
                nurse=random.choice(nurses)
            )
            
            patient.doctor.set(random.sample(doctors, random.randint(1, 3)))
            
            patients.append(patient)
        self.stdout.write(self.style.SUCCESS('Created 50 patients'))

        for patient in patients:
            hospital = Hospital.objects.create(
                patient=patient,
                nurse=random.choice(nurses)
            )
            
            hospital.doctor.set(random.sample(doctors, random.randint(1, 3)))
            
        self.stdout.write(self.style.SUCCESS('Created hospital 50 records for patients'))

        for patient in patients:
            medical_record = MedicalRecord.objects.create(
                patient=patient,
                diagnoses=fake.text(),
                prescription=fake.text()
            )
        self.stdout.write(self.style.SUCCESS('Created medical 50 records for patients'))
