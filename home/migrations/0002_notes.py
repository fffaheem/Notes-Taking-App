# Generated by Django 5.0.6 on 2024-05-28 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('title', models.TextField()),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
