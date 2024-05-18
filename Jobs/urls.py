from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_main, name='job_main'),
    path('<slug:slug>/', views.job_detail, name='job_detail'),
    path('joblist', views.job_list, name = "joblist")
]
