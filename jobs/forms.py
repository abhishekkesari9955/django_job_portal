from django import forms
from applications.models import Application
from .models import Job


class JobForm(forms.ModelForm):

    class Meta:
        model = Job

        fields = [
            "title",
            "description",
            "company",
            "location",
            "salary",
            "experience",
            "job_type",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6
                }
            ),

            "company": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "salary": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "experience": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "job_type": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
        }

class ApplicationStatusForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ["status"]

        widgets = {
            "status": forms.Select(
                attrs={
                    "class": "form-select"
                }
            )
        }