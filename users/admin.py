from django.contrib import admin
from .models import User, Helper

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'location')
    search_fields = ('full_name', 'email', 'phone', 'location')

@admin.register(Helper)
class HelperAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'gender', 'age', 'location', 'experience_years', 'rating')
    search_fields = ('full_name', 'email', 'phone', 'location', 'skills', 'languages')
    list_filter = ('gender', 'location', 'experience_years')
    ordering = ('-rating',)


