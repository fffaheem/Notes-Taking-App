# Generated by Django 5.0.6 on 2024-05-30 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_all_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='all_users',
        ),
    ]
