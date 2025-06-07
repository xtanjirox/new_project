from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'phone', 'position')
    list_filter = ('company',)
    search_fields = ('user__username', 'user__email', 'phone', 'position')
    list_per_page = 20