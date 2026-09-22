from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username

class RecruiterProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    company = models.CharField(max_length=200)

    phone = models.CharField(max_length=15)

    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username