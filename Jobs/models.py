
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

# class Jobs


# id
# Job Title
# Short Desc
# Long Desc
# companyName
# image
# how_to_apply_video 

# add these
# i want to add these fields to the job model
class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = self.model.Status.PUBLISHED)

# main job model

class Job(models.Model):
    
    class Status(models.TextChoices):
        DRAFT ='DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    job_title = models.CharField(max_length=250)
    job_title_hindi = models.CharField(max_length=250, blank= True)
    job_tag = models.CharField(max_length=250, blank= True)
    slug = models.SlugField(max_length=250, unique_for_date='date_posted', default = "")
    short_description = models.TextField()
    short_description_hindi = models.TextField(default = "")
    long_description = models.TextField(default = "")
    long_description_hindi = models.TextField(default = "")
    company_name = models.CharField(max_length=250)
    company_name_hindi = models.CharField(max_length=250)
    location = models.CharField(max_length=250 )
    image = models.ImageField(upload_to='job_images',null=True)
    how_to_apply_video = models.URLField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  
    date_posted = models.DateTimeField(default=timezone.now)
    objects = models.Manager() # The default manager
    published = PublishManager() # The costom manager
    status = models.CharField(max_length=2,choices = Status.choices, default = Status.DRAFT)

    
    

    
    
    

    class Meta:
        ordering = ['-date_posted']
        indexes = [
            models.Index(fields=['date_posted']),
        ]
    def __str__(self):
        return self.job_title
    


# Job Important Dates
class JobImportantDates(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    name_hindi = models.CharField(max_length=250, default= "")
    value = models.DateTimeField()

    def __str__(self):
        return self.name


# job Application fees

# id
# job_id
# name
# value

class JobApplicationFees(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    fees_name = models.CharField(max_length=250)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.fees_name

# Jobs Qualify age
# id
# job_id
# name
# value

class JobQualifyAge(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __int__(self):
        return self.job

# Jobs opening
# id
# job_id
# name
# no_of_opening
# desc

class JobOpening(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    name_hindi = models.CharField(max_length=250, default= "")
    no_of_opening = models.IntegerField()
    desc = models.TextField()

    def __str__(self):
        return self.name


# job_apply_links
# id
# link
# desc

class jobApplyLinks(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    link = models.URLField()
    desc = models.TextField()
    desc_hindi = models.TextField(default= "")
    def __str__(self):
        return self.link

# FAQ
# id
# job_id
# question
# asnwer

class FAQ(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    question = models.TextField()
    question_hindi = models.TextField(default= "")
    answer = models.TextField()
    answer_hindi = models.TextField(default= "")
    def __str__(self):
        return self.question
    
# job tag
# 
class Tags(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    Tagss = models.CharField(max_length=100)
    is_important = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    category_flags = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Concatenate boolean fields into a single string
        self.category_flags = ",".join([
            str(int(self.is_important)),
            str(int(self.is_active)),
            str(int(self.is_featured))
        ])
        super().save(*args, **kwargs)
    

# class PublishManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(status = self.model.Status.PUBLISHED)


# class Job(models.Model):
    
#     class Status(models.TextChoices):
#         DRAFT ='DF', 'Draft'
#         PUBLISHED = 'PB', 'Published'
        
#     job_title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250, unique_for_date='created')
#     job_description = models.TextField()
#     company = models.CharField(max_length=250)
#     location = models.CharField(max_length=250)
#     salary = models.CharField(max_length=250)
#     application_deadline = models.DateTimeField()
#     application_form_fields = models.TextField()
#     contact_information = models.BooleanField(default = False)
#     references = models.BooleanField(default = False)
#     equal_opportunity_employer = models.BooleanField(default = False)
#     privacy_policy = models.BooleanField(default = False)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
    
#     status = models.CharField(max_length=2,choices = Status.choices, default = Status.DRAFT)
    
#     objects = models.Manager() # The default manager
#     published = PublishManager() # The costom manager
#     class Meta:
#         ordering = ['-created']
#         indexes = [
#             models.Index(fields=['created']),
#         ]
    
#     def __str__(self):
#         return self.title
