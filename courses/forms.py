from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager
from django import forms
from django.shortcuts import render 



class UserManager(BaseUserManager):
    def create_superuser(self , username , email , password ):
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            password = password,
            is_staff = True
        )
        user.save(self._db)
        return user

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


# class Myforms(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username' , 'password')
#         widgets = {
#             'username' : forms.TextInput(attrs={'class' : 'form-control'}),
#             'password' : forms.TextInput(attrs={'class' : 'form-control'}),

#         }
