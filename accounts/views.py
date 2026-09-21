from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout

from .forms import RegistrationForm


def home(request):
    return render(request, "home.html")


def register(request):

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        print("POST RECEIVED")
        print("FORM DATA:", request.POST)

        if form.is_valid():

            print("FORM IS VALID")

            form.save()

            print("USER SAVED")

            return redirect("login")

        else:

            print("FORM IS NOT VALID")
            print(form.errors)

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