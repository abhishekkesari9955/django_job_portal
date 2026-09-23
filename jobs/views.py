from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job


def job_list(request):
    jobs = Job.objects.all()

    return render(request, "jobs/job_list.html", {
        "jobs": jobs
    })


def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    return render(request, "jobs/job_detail.html", {
        "job": job
    })

@login_required
def candidate_dashboard(request):
    return render(request,"accounts/dashboard.html")