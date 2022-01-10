# Generated by Django 3.2.8 on 2021-10-26 10:57

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0013_profile_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, default='pw4.jpg.url', max_length=255, null=True),
        ),
    ]