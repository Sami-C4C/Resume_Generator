from django.db import models


class Resume_Detail(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.TextField(max_length=1000, default='Default address')
    country = models.CharField(max_length=500)
    region = models.CharField(max_length=500)
    occupation = models.CharField(max_length=500)
    dob = models.DateField(default='None')
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    education = models.CharField(max_length=200)
    work_experience = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)
    hobbies = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='resume_photos/', blank=True, null=True)
