# Generated by Django 4.2.1 on 2023-05-27 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_details', '0002_resume_detail_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume_detail',
            name='school',
        ),
        migrations.AddField(
            model_name='resume_detail',
            name='address',
            field=models.TextField(default='Default address', max_length=500),
        ),
    ]
