from django.db import models


class Resume_Detail(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    address = models.TextField(max_length=1000, default='Default address')
    country = models.CharField(max_length=500, blank=False)
    region = models.CharField(max_length=500, blank=False)
    occupation = models.CharField(max_length=500,blank=False)
    dob = models.DateField(default='None')
    email = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=200, blank=False)
    degree = models.CharField(max_length=200, blank=False)
    summary = models.TextField(max_length=2000)
    education = models.CharField(max_length=200)
    work_experience = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)
    hobbies = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='resume_photos/', blank=True, null=True)
