from django.db import models
from django.contrib.auth.models import User

from jobs.models import Job

# Create your models here.
class Application(models.Model):
    STATUS_CHOICES = [
        ('applied','Applied'),
        ('shortlisted','Shortlisted'),
        ('rejected','Rejected'),
        ('hired','Hired'),]

    candidate = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE , related_name='applications')
    cover_letter = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.username} - {self.job.title}"  