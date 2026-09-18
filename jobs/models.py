from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title