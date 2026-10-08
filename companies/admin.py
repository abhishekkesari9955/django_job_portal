from django.contrib import admin
from .models import Company
# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'email', 'created_at')
    search_fields = ('name', 'location', )
    