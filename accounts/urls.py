from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/",views.logout_view, name="logout"),
    path("candidate/dashboard/", views.candidate_dashboard, name="candidate_dashboard"),
    path("recruiter/dashboard/", views.recruiter_dashboard, name="recruiter_dashboard"),
    path("candidate/profile/", views.candidate_profile, name="candidate_profile"),
]