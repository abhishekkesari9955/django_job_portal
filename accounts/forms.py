from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import CandidateProfile


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    ROLE_CHOICES = [
        ("candidate", "Candidate"),
        ("recruiter", "Recruiter"),
    ]

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "role",
        ]
class CandidateProfileForm(forms.ModelForm):

    class Meta:
        model = CandidateProfile

        fields = [
            "phone",
            "skills",
            "user",
            "experience",
            "location",
            "resume",
        ]