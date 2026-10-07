from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm , ApplicationStatusForm
from applications.models import Application
from django.core.paginator import Paginator

def job_list(request):
    query = request.GET.get("q",'')
    job_type = request.GET.get("job_type",'')
    location = request.GET.get("location",'')
    jobs = Job.objects.all()
    if query:
        jobs = jobs.filter(title__icontains=query) | jobs.filter(description__icontains=query) | jobs.filter(location__icontains=query)
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    if location:
        jobs = jobs.filter(location__icontains=location)
    
    jobs = jobs.order_by("-created_at")
    paginator = Paginator(jobs, 6)
    page_number = request.GET.get("page")
    jobs = paginator.get_page(page_number)

    return render(request, "jobs/job_list.html", {
        "jobs": jobs,
        "page_obj": jobs,
        "query": query,
        "job_type": job_type,
        "location": location
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
            job.recruiter = request.user
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

@login_required
def edit_job(request, job_id):
    if not hasattr(request.user, "recruiterprofile"):
        return redirect("home")

    job = get_object_or_404(Job,id=job_id,recruiter=request.user)

    if request.method == "POST":
        form = JobForm(request.POST, instance=job)

        if form.is_valid():
            form.save()
            return redirect("recruiter_jobs")
    else:
        form = JobForm(instance=job)
    return render(request,"jobs/edit_job.html",{"form": form, "job": job})

@login_required
def delete_job(request, job_id):
    if not hasattr(request.user, "recruiterprofile"):
        return redirect("home")

    job = get_object_or_404(Job,id=job_id,recruiter=request.user)

    if request.method == "POST":
        job.delete()
        return redirect("recruiter_jobs")

    return render(request,"jobs/delete_job.html",{"job": job})

@login_required
def job_applicants(request, job_id):
    if not hasattr(request.user, "recruiterprofile"):
        return redirect("home")

    job = get_object_or_404(Job,id=job_id,recruiter=request.user)

    applications = job.applications.select_related("candidate").order_by("-applied_at")

    return render(request,"jobs/job_applicants.html",{"job": job,"applications": applications})

@login_required
def application_detail(request, application_id):
    if not hasattr(request.user, "recruiterprofile"):
        return redirect("home")

    application = get_object_or_404(Application,id=application_id,job__recruiter=request.user)

    candidate = application.candidate

    return render(request,"jobs/application_detail.html",{"application": application,"candidate": candidate,})

@login_required
def update_application_status(request, application_id):

    if not hasattr(request.user, "recruiterprofile"):
        return redirect("home")

    application = get_object_or_404(
        Application,
        id=application_id,
        job__recruiter=request.user
    )

    if request.method == "POST":

        form = ApplicationStatusForm(
            request.POST,
            instance=application
        )

        if form.is_valid():
            form.save()
            return redirect(
                "application_detail",
                application_id=application.id
            )

    else:
        form = ApplicationStatusForm(instance=application)

    return render(
        request,
        "jobs/update_application_status.html",
        {
            "form": form,
            "application": application
        }
    )