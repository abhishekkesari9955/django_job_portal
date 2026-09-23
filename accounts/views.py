from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from .forms import RegistrationForm, CandidateProfileForm
from .models import CandidateProfile, RecruiterProfile
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")

def register(request):

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            role = form.cleaned_data["role"]

            if role == "candidate":

                CandidateProfile.objects.create(
                    user=user
                )

            elif role == "recruiter":

                RecruiterProfile.objects.create(
                    user=user
                )

            return redirect("login")

    else:

        form = RegistrationForm()

    return render(request, "accounts/register.html", {
        "form": form
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)

            if hasattr(user, "candidateprofile"):
                return redirect("candidate_dashboard")

            elif hasattr(user, "recruiterprofile"):
                return redirect("recruiter_dashboard")

            return redirect("home")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid username or password."})
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def candidate_dashboard(request):
    if not hasattr(request.user, "candidateprofile"):
        return redirect("home")
    return render(request, "accounts/candidate_dashboard.html")
@login_required
def recruiter_dashboard(request):
    if not hasattr(request.user, "recruiterprofile"):
        return redirect("home")
    return render(request, "accounts/recruiter_dashboard.html")

@login_required
def candidate_profile(request):

    profile = request.user.candidateprofile

    if request.method == "POST":

        form = CandidateProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect("candidate_profile")

    else:
        form = CandidateProfileForm(instance=profile)

    return render(
        request,
        "accounts/candidate_profile.html",
        {"form": form}
    )