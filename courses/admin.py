from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Courses ,Cart , Student , Teacher
# Register your models here.


# admin.site.register(CustomUser , UserModel)
admin.site.register(Courses)
admin.site.register(Cart)
admin.site.register(Student)
admin.site.register(Teacher)
