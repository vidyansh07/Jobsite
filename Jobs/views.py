from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Job
from django.core.paginator import Paginator

def job_main(request):
    jobs = Job.published.all()
    card = 1
    return render(request, 'jobs/job_main.html', {'jobs': jobs,
                                                  "card": card})


def job_detail(request, slug):
    job = get_object_or_404(Job.published, slug=slug)
    return render(request, 'jobs/job_detail.html', {'job': job})


def job_list(request):
    job_list = Job.published.all()  # Replace with your query
    paginator = Paginator(job_list, 10)  # Show 10 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/job_list.html', {'page_obj': page_obj})
