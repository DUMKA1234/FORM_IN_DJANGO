from django.shortcuts import render, redirect
from .form import EmploymentApplicationForm
from .form import JobExperienceForm
from .form import BioDataForm

def employment_application_view(request):
    if request.method == 'POST':
        form = EmploymentApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_experience_view')
    else:
        form = EmploymentApplicationForm()
    return render(request, 'employment_application.html', {'form': form})

def job_experience_view(request):
    if request.method == 'POST':
        form = JobExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bio_data_view')
    else:
        form = JobExperienceForm()
    return render(request, 'job_experience.html', {'form': form})

def bio_data_view(request):
    if request.method == 'POST':
        form = BioDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('education_view')
    else:
        form = BioDataForm()
    return render(request, 'bio_data.html', {'form':form})