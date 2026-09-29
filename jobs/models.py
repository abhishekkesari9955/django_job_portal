from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time','Full Time'),
        ('part-time','Part Time'),
        ('internship','Internship'),
        ('contract','Contract'),
        
    ]

    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs',null=True,
    blank=True)

    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50,choices=JOB_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title