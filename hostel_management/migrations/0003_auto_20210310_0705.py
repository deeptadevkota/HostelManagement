# Generated by Django 2.2.12 on 2021-03-10 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_management', '0002_warden_block_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warden',
            name='block_name',
        ),
        migrations.AddField(
            model_name='building',
            name='block_name',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='hostel_management.Warden'),
        ),
    ]
