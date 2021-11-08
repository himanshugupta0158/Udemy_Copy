# Generated by Django 3.2.9 on 2021-11-01 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('skills', models.TextField()),
                ('joining_on', models.DateField(auto_now_add=True)),
                ('pic_path', models.FileField(upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author_name', models.CharField(max_length=50)),
                ('video', models.FileField(upload_to='videos/')),
            ],
        ),
    ]
