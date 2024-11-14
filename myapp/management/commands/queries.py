# Task-1:
# Retrieve all patients admitted on a specific date.
from datetime import datetime
from myapp.models import Patient 
specific_date = datetime(2024, 11, 11)
patients_on_date = (Patient.objects
    .filter(date_admitted__date=specific_date)
    .values('name', 'age', 'date_admitted')) 



# - Get the names of all doctors who have patients with a specific diagnosis.
from myapp.models import Doctor  
specific_diagnosis = "Several word including whose go finally"
doctors_with_specific_diagnosis = (Doctor.objects
    .filter(patients__medical_records__diagnoses__icontains=specific_diagnosis)
    .select_related('department')  
    .distinct()
    .values_list('name', flat=True)) 


# - Find all patients treated by a particular nurse.
from myapp.models import Patient, Nurse  
nurse_name = 'Corey Jones'
patients_treated_by_nurse = (Patient.objects
    .filter(nurse__name=nurse_name)
    .select_related('nurse')
    .values('name', 'age', 'date_admitted', 'nurse__name')) 



# - Retrieve the contact number of the doctor for a given patient.
from myapp.models import Patient 
patient_name = 'Rachel Martinez' 
try:
    patient = Patient.objects.get(name=patient_name)  
except Patient.DoesNotExist:
    print(f"Patient with ID {patient_name} does not exist.")
else:
    doctors = patient.doctor.all()  
    if doctors:
        print(f"Contact numbers for doctors treating {patient.name}:")
        for doctor in doctors:
            print(f"{doctor.name}: {doctor.contact_number}")
    else:
        print(f"No doctors assigned to patient {patient.name}.")


# - Get the total number of patients admitted to a hospital.
from myapp.models import Patient  
total_patients = Patient.objects.count()
print(f"Total number of patients admitted to the hospital: {total_patients}")


# - Find the patients who are not assigned to any nurse.
from myapp.models import Patient 
patients_without_nurse = (Patient.objects
    .filter(nurse__isnull=True)
    .values('name', 'age', 'date_admitted'))



# - Retrieve the names of nurses who have patients with a specific prescription.
from myapp.models import Nurse  
specific_prescription = "Bit race his major American..."
nurses_with_prescription = (Nurse.objects
    .filter(patients__medical_records__prescription__icontains=specific_prescription
    )
    .distinct()
    .values_list('name', flat=True))




# - Get the average age of patients in the hospital.
from django.db.models import Avg
from myapp.models import Patient  
average_age = Patient.objects.aggregate(aggregated_resut=Avg('age'))['aggregated_resut']



# - Find the most recently admitted patient.
from myapp.models import Patient 
most_recent_patient = (Patient.objects
    .order_by('-date_admitted')
    .only('name', 'age', 'date_admitted')
    .first())





# - Retrieve all doctors who have more than five patients.
from django.db.models import Count
from myapp.models import Doctor 
doctors_with_many_patients = (Doctor.objects
    .annotate(patient_count=Count('patients'))
    .filter(patient_count__gt=5)
    .values('name', 'patient_count'))



# - Find the patients who have been admitted for more than a week.
from django.utils import timezone
from datetime import timedelta
from myapp.models import Patient  
one_week_ago = timezone.now() - timedelta(weeks=1)
long_term_patients = (Patient.objects
    .filter(date_admitted__lt=one_week_ago)
    .only('name', 'age', 'date_admitted'))


# - Get the number of patients assigned to each nurse.
from django.db.models import Count
from myapp.models import Nurse  
nurse_patient_counts = (Nurse.objects
    .annotate(patient_count=Count('patients'))
    .values('name', 'patient_count')
    .order_by('-patient_count'))




# - Find the doctors who specialize in a specific medical field.
from myapp.models import Doctor  
specific_specialization = "Pharmacist, community"  
doctors_with_specific_specialization = Doctor.objects.filter(specialization=specific_specialization)




# - Retrieve the latest medical record for a given patient.

from myapp.models import MedicalRecord, Patient  
patient_name = "Travis Curry"
patient = Patient.objects.get(name=patient_name)
latest_medical_record = MedicalRecord.objects.filter(patient=patient).order_by('-patient__date_admitted').first()



# - Get the names of patients with a specific diagnosis.
from myapp.models import MedicalRecord  
specific_diagnosis = "Kid various various appear better weight. Spring ball people future under entire. Population actually second management themselves."  
patients_with_specific_diagnosis = MedicalRecord.objects.filter(diagnoses__icontains=specific_diagnosis).select_related('patient')






# - Find the doctors who have patients of a certain age group.
from myapp.models import Patient, Doctor 
min_age = 30  
max_age = 50  
patients_in_age_group = Patient.objects.filter(range=(min_age, max_age))
doctors_with_patients_in_age_group = Doctor.objects.filter(patients__in=patients_in_age_group).distinct()


# - Retrieve all patients with a specific prescription.
from myapp.models import MedicalRecord  
specific_prescription = "Toward either land easy bed sometimes. Suddenly still believe trouble politics." 
medical_records_with_specific_prescription = MedicalRecord.objects.filter(prescription__icontains=specific_prescription)





# - Find the nurses who have patients with a specific age.
from myapp.models import Patient, Nurse
specific_age = 25
patients_with_specific_age = Patient.objects.filter(age=specific_age)
nurses_with_patients_of_specific_age = Nurse.objects.filter(patients__in=patients_with_specific_age).distinct()




# - Get the total number of medical records in the system.
from myapp.models import MedicalRecord 
total_medical_records = MedicalRecord.objects.count()
print(f"Total number of medical records in the system: {total_medical_records}")


# - Retrieve the names of patients treated by a nurse with a specific contact number.
from myapp.models import Nurse, Patient 
specific_contact_number = "(599)836-3996x35829" 
nurse = Nurse.objects.get(contact_number=specific_contact_number)
patients = nurse.patients.all()




# - Find the patients who are treated by more than one doctor.
from django.db.models import Count
from myapp.models import Patient 
patients_with_multiple_doctors = (Patient.objects
    .annotate(num_doctors=Count('doctor'))
    .filter(num_doctors__gt=1)
    .values('name', 'num_doctors')
    .order_by('name'))



# - Get the names of doctors who have treated patients with a specific prescription.

from myapp.models import MedicalRecord, Patient, Doctor  
from django.db.models import Q
specific_prescription = "Admit wife buy throw method..."
doctors_with_prescription = (Doctor.objects
    .filter(
        Q(patients__medical_records__prescription__icontains=specific_prescription)
    )
    .distinct()
    .values_list('name', flat=True))



# - Find the patients who have not been assigned to any doctor.
from myapp.models import Patient 
patients_without_doctors = (Patient.objects
    .filter(doctor__isnull=True)
    .values_list('name', flat = True))



# - Retrieve the patients who have medical records with a specific prescription.

from myapp.models import Patient  
specific_prescription = "Admit wife buy throw method..."
patients_with_prescription = (Patient.objects
    .filter(medical_records__prescription__icontains=specific_prescription)
    .prefetch_related(
        Prefetch('medical_records', 
                queryset=MedicalRecord.objects.only('prescription'))
    )
    .distinct()
    .values_list('name', flat = True))



# - Get the total number of patients treated by nurses in a specific specialization.
from myapp.models import Nurse, Patient 
from django.db.models import Count
specific_specialization = "Pediatrics" 
total_patients = Patient.filter(nurse__specialization=specific_specialization).distinct().count()


# - Retrieve the patients who have not been assigned to any nurse.

from myapp.models import Patient  
patients_without_nurses = (Patient.objects
    .filter(nurse__isnull=True)
    .only('name', 'id')
    .order_by('name'))



# - Retrieve the doctors who have patients with a specific diagnosis and age group.

from myapp.models import Patient, MedicalRecord, Doctor 
specific_diagnosis = "Control popular art south. American travel glass stuff. Enter red ever table represent similar. Behind agree yourself. Black check you."  
age_min = 30       
age_max = 50       
doctors_with_specific_patients = Doctor.objects.filter(
            Q(patients__medical_records__diagnoses__icontains=specific_diagnosis) &
            Q(patients__age__range=(age_min, age_max))
        ).distinct().values('name', 'specialization')





# - Get the number of patients treated by each nurse in a specific specialization.
from myapp.models import Nurse, Patient  
from django.db.models import Count
specific_specialization = "Pediatrics" 
nurses_with_patient_count = Nurse.objects.filter(specialization=specific_specialization).annotate(
            patient_count=Count('patients', distinct=True)).values('name', 'patient_count').order_by('-patient_count')



# - Retrieve the names of doctors who have patients with a specific diagnosis and age group.


from myapp.models import Patient, MedicalRecord, Doctor 
specific_diagnosis = "Hypertension" 
age_min = 40                    
age_max = 60                    
doctors_with_specific_patients = Doctor.objects.filter(
            Q(patients__medical_records__diagnoses__icontains=specific_diagnosis) &
            Q(patients__age__range=(age_min, age_max))
        ).annotate(
            patient_count=Count('patients', distinct=True)
        ).values('name', 'specialization', 'patient_count'
        ).order_by('-patient_count')





# Task 2:

# - Select all patients with their associated doctors and nurses.

from myapp.models import Patient  
patients_with_associations = Patient.objects.prefetch_related('doctor', 'nurse')
for patient in patients_with_associations:
    doctor_names = ", ".join([doctor.name for doctor in patient.doctor.all()])  
    nurse_name = patient.nurse.name if patient.nurse else "No nurse assigned" 
    print(f"Patient: {patient.name}, Age: {patient.age}, Doctors: [{doctor_names}], Nurse: {nurse_name}")


# - Select all patients admitted after a specific date.

from myapp.models import Patient  
from datetime import datetime
specific_date = datetime(2024, 11, 1) 
patients_admitted_after_date = Patient.objects.filter(date_admitted__gt=specific_date)
if patients_admitted_after_date.exists():
    print(f"Patients admitted after {specific_date.date()}:")
    for patient in patients_admitted_after_date:
        print(f"Patient: {patient.name}, Age: {patient.age}, Date Admitted: {patient.date_admitted}")
else:
    print(f"No patients found admitted after {specific_date.date()}.")


# - Count the total number of patients.

from myapp.models import Patient  
total_patients = Patient.objects.count()
print(f"Total number of patients: {total_patients}")


# - Count the total number of patients with a specific age.
from myapp.models import Patient 
specific_age = 30
total_patients_with_specific_age = Patient.objects.filter(age=specific_age).count()
print(f"Total number of patients with age {specific_age}: {total_patients_with_specific_age}")



# - Select all patients with their associated doctors and nurses prefetched.

from myapp.models import Patient  
patients_with_associations = Patient.objects.prefetch_related('doctor').select_related('nurse')
for patient in patients_with_associations:
    doctor_names = ", ".join([doctor.name for doctor in patient.doctor.all()]) 
    nurse_name = patient.nurse.name if patient.nurse else "No nurse assigned"  
    print(f"Patient: {patient.name}, Age: {patient.age}, Doctors: [{doctor_names}], Nurse: {nurse_name}")


# - Count the total number of doctors associated with each patient.
from myapp.models import Patient  
patients = Patient.objects.prefetch_related('doctor').aggregate
for patient in patients:
    doctor_count = patient.doctor.count()  
    print(f"Patient: {patient.name}, Total Doctors: {doctor_count}")


# - Sum the ages of all patients.
from django.db.models import Sum
from myapp.models import Patient  
total_age = Patient.objects.aggregate(Sum('age'))
sum_of_ages = total_age['age__sum'] or 0  # Use or 0 to handle cases where there are no patients
print(f"Total sum of ages of all patients: {sum_of_ages}")


# - Select all patients along with the number of doctors associated with each.

from django.db.models import Count
from myapp.models import Patient  
patients_with_doctor_count = Patient.objects.annotate(doctor_count=Count('doctor'))
for patient in patients_with_doctor_count:
    print(f"Patient: {patient.name}, Total Doctors: {patient.doctor_count}")


# - Select all patients along with their medical records, if available.

from myapp.models import Patient  
patients_with_medical_records = Patient.objects.prefetch_related('medical_records')
for patient in patients_with_medical_records:
    medical_records = patient.medical_records.all()  #
    records_count = medical_records.count() 
    print(f"Patient: {patient.name}, Age: {patient.age}, Medical Records: {records_count}")
    if records_count > 0:
        for record in medical_records:
            print(f"  # - Medical Record: Diagnoses: {record.diagnoses}, Prescription: {record.prescription}")
    else:
        print("  # - No medical records available.")

    

# - Count the total number of nurses associated with each patient.

from django.db.models import Count
from myapp.models import Patient  
patients_with_nurse_count = Patient.objects.annotate(nurse_count=Count('nurse'))
for patient in patients_with_nurse_count:
    print(f"Patient: {patient.name}, Total Nurses: {patient.nurse_count}")


# - Select all patients with their associated nurses and the nurses' contact numbers.

from myapp.models import Patient 
patients_with_nurses = Patient.objects.select_related('nurse')
for patient in patients_with_nurses:
    nurse_contact = patient.nurse.contact_number  # Access the nurse's contact number
    print(f"Patient: {patient.name}, Age: {patient.age}, Nurse: {patient.nurse.name}, Nurse Contact: {nurse_contact}")


# - Select all patients along with the total number of medical records for each.

from django.db.models import Count
from myapp.models import Patient  
patients_with_record_count = Patient.objects.annotate(record_count=Count('medical_records'))
for patient in patients_with_record_count:
    print(f"Patient: {patient.name}, Age: {patient.age}, Total Medical Records: {patient.record_count}")



# - Select all patients with their diagnoses and prescriptions, if available.

from myapp.models import Patient 
patients_with_records = Patient.objects.prefetch_related('medical_records')
for patient in patients_with_records:
    print(f"Patient: {patient.name}, Age: {patient.age}")
    medical_records = patient.medical_records.all()  # Get all medical records for the patient
    if medical_records.exists():  # Check if there are any medical records
        for record in medical_records:
            print(f"  # - Diagnosis: {record.diagnoses}, Prescription: {record.prescription}")
    else:
        print("  # - No medical records available.")


# - Count the total number of patients admitted in a specific year.

from django.utils import timezone
from myapp.models import Patient 
specific_year = 2024  
total_patients = Patient.objects.filter(date_admitted__year=specific_year).count()
print(f"Total number of patients admitted in {specific_year}: {total_patients}")


# - Select all patients along with their doctors' specializations.

from myapp.models import Patient  
patients_with_doctor_specializations = Patient.objects.prefetch_related('doctor')
for patient in patients_with_doctor_specializations:
    print(f"Patient: {patient.name}, Age: {patient.age}")
    doctors = patient.doctor.all()  # Get all doctors associated with the patient
    if doctors.exists():  # Check if there are any doctors
        for doctor in doctors:
            print(f"  # - Doctor: {doctor.name}, Specialization: {doctor.specialization}")
    else:
        print("  # - No associated doctors.")

    

# - Select all patients along with the count of medical records for each.

from django.db.models import Count
from my.models import Patient 
patients_with_record_counts = Patient.objects.annotate(record_count=Count('medical_records'))
for patient in patients_with_record_counts:
    print(f"Patient: {patient.name}, Age: {patient.age}, Medical Records Count: {patient.record_count}")



# - Select all doctors with the count of patients they are associated with.
from django.db.models import Count
from myapp.models import Doctor  
doctors_with_patient_counts = Doctor.objects.annotate(patient_count=Count('patients'))
for doctor in doctors_with_patient_counts:
    print(f"Doctor: {doctor.name}, Specialization: {doctor.specialization}, Patients Count: {doctor.patient_count}")


# - Select all patients along with the count of nurses they are associated with.

from django.db.models import Count
from myapp.models import Patient 
patients_with_nurse_counts = Patient.objects.annotate(nurse_count=Count('nurse'))
for patient in patients_with_nurse_counts:
    print(f"Patient: {patient.name}, Age: {patient.age}, Nurses Count: {patient.nurse_count}")




# - Annotate the average age of patients.

from django.db.models import Avg
from myapp.models import Patient  
average_age = Patient.objects.aggregate(Avg('age'))
avg_age = average_age['age__avg']
print(f"The average age of patients is: {avg_age:.2f}")


# - Annotate the maximum age of patients.

from django.db.models import Max
from myapp.models import Patient  
maximum_age = Patient.objects.aggregate(Max('age'))
max_age = maximum_age['age__max']
if max_age is not None:
    print(f"The maximum age of patients is: {max_age}")
else:
    print("No patients available to determine the maximum age.")



# - Annotate the minimum age of patients.

from django.db.models import Min
from myapp.models import Patient  
minimum_age = Patient.objects.aggregate(Min('age'))
min_age = minimum_age['age__min']
if min_age is not None:
    print(f"The minimum age of patients is: {min_age}")
else:
    print("No patients available to determine the minimum age.")


# - Select all patients along with the earliest admission date.


from django.db.models import Min
from myapp.models import Patient
earliest_admission = Patient.objects.aggregate(Min('date_admitted'))
min_admission_date = earliest_admission['date_admitted__min']
patients_with_earliest_admission = Patient.objects.annotate(earliest_admission_date=Min('date_admitted'))
if min_admission_date is not None:
    for patient in patients_with_earliest_admission:
        print(f"Patient: {patient.name}, Admission Date: {patient.date_admitted}, Earliest Admission Date: {min_admission_date}")
else:
    print("No patients available to determine the earliest admission date.")



# - Select all doctors with their associated patients prefetched.
from django.db.models import Prefetch
from myapp.models import Doctor, Patient  
doctors_with_patients = Doctor.objects.prefetch_related('patients')
for doctor in doctors_with_patients:
    print(f"Doctor: {doctor.name}, Specialization: {doctor.specialization}")
    for patient in doctor.patients.all():
        print(f"  Patient: {patient.name}, Age: {patient.age}, Admission Date: {patient.date_admitted}")


# - Select all nurses with their associated patients prefetched.
from django.db.models import Prefetch
from myapp.models import Nurse, Patient 
nurses_with_patients = Nurse.objects.prefetch_related('patients')
for nurse in nurses_with_patients:
    print(f"Nurse: {nurse.name}")
    for patient in nurse.patients.all():
        print(f"  Patient: {patient.name}, Age: {patient.age}, Admission Date: {patient.date_admitted}")


# - Select all patients along with the count of distinct doctors they are associated with.
from django.db.models import Count
from myapp.models import Patient
patients_with_doctor_count = Patient.objects.annotate(distinct_doctor_count=Count('doctor', distinct=True))
for patient in patients_with_doctor_count:
    print(f"Patient: {patient.name}, Age: {patient.age}, Distinct Doctor Count: {patient.distinct_doctor_count}")













    



















