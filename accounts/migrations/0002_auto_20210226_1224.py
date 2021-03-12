# Generated by Django 3.1.7 on 2021-02-26 06:54

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profilePic',
            field=models.ImageField(blank=True, default='/employee/profile-picture.png', null=True, upload_to=accounts.models.documents_path),
        ),
    ]