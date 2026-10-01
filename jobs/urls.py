from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_list, name="job_list"),
    path("recruiter/create/", views.create_job, name="create_job"),
    path("recruiter/jobs/", views.recruiter_jobs, name="recruiter_jobs"),
    path("<int:job_id>/", views.job_detail, name="job_detail"),
    path("recruiter/jobs/<int:job_id>/edit/",views.edit_job,name="edit_job"),
    path("recruiter/jobs/<int:job_id>/delete/",views.delete_job,name="delete_job"),
]