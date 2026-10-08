from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company

        fields = [
            "name",
            "description",
            "location",
            "website",
            "email",
            "phone",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company Name"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "About your company"
            }),

            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company Location"
            }),

            "website": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://example.com"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "company@example.com"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number"
            }),
        }