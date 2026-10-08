from django.db import models

# Create your models here.



class Company(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    location = models.CharField(max_length=100)

    website = models.URLField(blank=True)

    email = models.EmailField(blank=True)

    phone = models.CharField(
        max_length=15,
        blank=True
    )
    recruiter= models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='companies',null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name