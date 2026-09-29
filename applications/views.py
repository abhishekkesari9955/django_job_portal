from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from jobs.models import Job
from .models import Application
from .forms import AppicationForm


# Create your views here.
@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if not hasattr((request.user), 'candidateprofile'):
        return redirect('home')
    if Application.objects.filter(candidate=request.user, job=job).exists():
        return render(request, 'applications/already_applied.html', {'job': job})
    if request.method == 'POST':
        form = AppicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.candidate = request.user
            application.job = job
            application.save()
            return redirect('application_success')
    else:
        form = AppicationForm()
    return render(request, 'applications/apply.html', {'form': form, 'job': job})


@login_required
def application_success(request):
    return render(request, 'applications/application_success.html')



def my_applications(request):
    if not request.user.is_authenticated:
        return redirect("home")
    applications = Application.objects.filter(
        candidate=request.user).select_related('job').order_by("-applied_at")
    return render(request,"applications/my_applications.html",{"applications":applications})

