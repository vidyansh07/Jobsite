from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Job


def job_list(request):
    jobs = Job.published.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def job_detail(request, slug):
    job = get_object_or_404(Job.published, slug=slug)
    return render(request, 'jobs/job_detail.html', {'job': job})
