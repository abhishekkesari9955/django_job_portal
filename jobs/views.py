from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm

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

@login_required
def create_job(request):
    if not hasattr(request.user, "recruiterprofile"):
        return redirect("home")

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recuiter =request.user
            job.save()
            return redirect("recruiter_jobs")
    else:
        form = JobForm()

    return render(request,"jobs/create_job.html",{"form":form})

@login_required
def recruiter_jobs(request):
    if not hasattr(request.user,"recruiterprofile"):
        return redirect("home")
    jobs = Job.objects.filter(recruiter=request.user).order_by("-created_at")
    return render(request,"jobs/recruiter_jobs.html",{"jobs":jobs})
