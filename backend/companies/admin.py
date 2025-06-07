from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'tva_rate', 'created_at')
    list_filter = ('created_at',)
    list_per_page = 20
