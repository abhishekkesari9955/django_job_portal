from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('<int:company_id>/', views.company_detail, name='company_detail'),
    path('manage/', views.manage_company, name='manage_company'),
]