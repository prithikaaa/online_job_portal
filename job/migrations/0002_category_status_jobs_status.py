# Generated by Django 4.2.3 on 2023-08-04 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=False, help_text='0=default, 1=Hidden'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='status',
            field=models.BooleanField(default=False, help_text='0=default, 1=Hidden'),
        ),
    ]
