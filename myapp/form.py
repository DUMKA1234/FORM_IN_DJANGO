from django import forms
from .models import EmploymentApplication, BioData, JobExperience

class EmploymentApplicationForm(forms.ModelForm):
    class Meta:
        model = EmploymentApplication
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'address')

class BioDataForm(forms.ModelForm):
    class Meta:
        model = BioData
        fields = ('date_of_birth', 'place_of_birth', 'nationality')

class JobExperienceForm(forms.ModelForm):
    class Meta:
        model = JobExperience
        fields = ('company', 'job_title', 'start_date', 'end_date')