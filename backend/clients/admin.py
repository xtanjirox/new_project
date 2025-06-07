from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'contact_person', 'email', 'phone', 'created_at')
    list_filter = ('company', 'created_at')
    search_fields = ('name', 'contact_person', 'email', 'phone')
    list_per_page = 20
