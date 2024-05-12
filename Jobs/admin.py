# admin.py

from django.contrib import admin
from .models import Job, JobImportantDates, JobApplicationFees, JobQualifyAge, JobOpening, jobApplyLinks, FAQ, Tags

class JobImportantDatesInline(admin.StackedInline):
    model = JobImportantDates
    extra =1 

class JobApplicationFeesInline(admin.StackedInline):
    model = JobApplicationFees
    extra = 1

class JobQualifyAgeInline(admin.StackedInline):
    model = JobQualifyAge
    extra = 1

class JobOpeningInline(admin.StackedInline):
    model = JobOpening
    extra = 1

class jobApplyLinksInline(admin.StackedInline):
    model = jobApplyLinks
    extra = 1

class FAQInline(admin.StackedInline):
    model = FAQ
    extra = 1

class TagsInline(admin.StackedInline):
    model = Tags
    extra = 1
    
    

class JobAdmin(admin.ModelAdmin):
    inlines = [JobImportantDatesInline, JobApplicationFeesInline, JobQualifyAgeInline, JobOpeningInline, jobApplyLinksInline, FAQInline, TagsInline]
    tag=TagsInline.model
    list_display = ('job_title', 'company_name', 'location', 'created_by', 'tag', )
    search_fields = ('job_title', 'company_name', 'location', 'created_by')
    list_filter = ('created_by', 'location')
    ordering = ['created_by', 'location']
    prepopulated_fields = {'slug': ('job_title',)}

admin.site.register(Job, JobAdmin)
