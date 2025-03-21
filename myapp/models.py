from django.db import models

class EmploymentApplication(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

class BioData(models.Model):
    employment_application = models.OneToOneField(EmploymentApplication, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)

class JobExperience(models.Model):
    employment_application = models.ForeignKey(EmploymentApplication, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()