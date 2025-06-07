from django.contrib import admin
from .models import Company, Currency

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'tva_rate', 'created_at')
    list_filter = ('created_at',)
    list_per_page = 20

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'symbol')
    search_fields = ('code', 'name')
