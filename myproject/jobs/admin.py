from django.contrib import admin
from .models import JobListing

class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'salary_min', 'salary_max', 'job_type', 'shift', 'date_posted')
    search_fields = ('title', 'company', 'job_type', 'shift')
    list_filter = ('job_type', 'shift', 'date_posted')
    ordering = ('-date_posted',)  # Orders by date_posted in descending order

admin.site.register(JobListing, JobListingAdmin)
