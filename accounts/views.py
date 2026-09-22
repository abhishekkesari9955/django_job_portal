from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from .forms import RegistrationForm
from .models import CandidateProfile, RecruiterProfile


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
            return redirect("home")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid username or password."})
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("home")