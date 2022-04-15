from django.contrib import admin
from .models import Resume
# Register your models here.
@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'email', 'gender', 'profile_image', 'mobile', 'locality', 'city', 'pin', 'state', 'job_city', 'file']
