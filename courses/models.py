from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.


class Courses(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length = 150)
    created_on = models.DateTimeField(auto_now_add=True)
    Teacher_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    video = models.FileField(upload_to='videos/')


    def __str__(self):
        return self.title


class Buy(models.Model):
    buyer = models.CharField(max_length = 150)
    course = models.CharField(max_length=150)



class Cart(models.Model):
    courses = models.CharField(max_length = 150)
    name = models.CharField(max_length = 150)




class Teacher(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    profile_pic=models.FileField()
    Email_address=models.TextField()
    gender=models.CharField(max_length=25)
    profession = models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    skills = models.CharField(max_length = 250)




class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    profile_pic=models.FileField()
    gender=models.CharField(max_length=25)
    profession = models.CharField(max_length=250)
    Email_address=models.TextField()
    updated_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)



