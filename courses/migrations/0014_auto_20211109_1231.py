# Generated by Django 3.2.8 on 2021-11-09 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_courses_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='address',
            new_name='Email_address',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='address',
            new_name='Email_address',
        ),
    ]
