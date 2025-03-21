from django.urls import path
from django.urls import path
from . import views
urlpatterns=[
    path('application/', views.application, name='application'),
    path('biodata/', views.biodata, name='biodata'),
    path('education/', views.education, name='education'),
    path('jobexperience/', views.jobexperience, name='jobexperience'),
    path('role/', views.role, name='role'),
    path('success/', views.success, name='success'), 
]
    
