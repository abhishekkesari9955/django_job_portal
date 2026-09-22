from django.contrib import admin
from .models import CandidateProfile, RecruiterProfile

# Register your models here.
admin.site.register(CandidateProfile)
admin.site.register(RecruiterProfile)