from django import forms
from .models import Application


class AppicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter']
        widgets = {
            'cover_letter' : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 6,
                    'placeholder':' write your cover letter...'
                }
            )
        }