# Generated by Django 3.2.8 on 2021-10-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0010_auto_20211019_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='pw4.jpg.url', null=True, upload_to='profile/'),
        ),
    ]
