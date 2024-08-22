from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'name':"username",'id':"email",'class':"form-control",'placeholder':"Username"}))
    password1=forms.CharField(widget=forms.TextInput(attrs={'name':"password1",'id':"password",'class':"form-control",'placeholder':"password"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={'name':"password2",'id':"confirm_password",'class':"form-control",'placeholder':"confirm password"}))
    
    class Meta:
        model=User
        fields=['username']
    
class ProfileForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'type':"text",'name':"name",'placeholder':"Name"}))
    email=forms.CharField(widget=forms.TextInput(attrs={'type':"email",'name':"email",'placeholder':"Email"}))
    pic=forms.ImageField(widget=forms.FileInput(attrs={'type':"file",'name':"image",'required':False}))
    dob=forms.DateField(widget=forms.DateInput(attrs={'type':"date",'name':"dob"}))
    class Meta:
        model=Profile
        fields=['name','pic','dob','email']    

class AlbumnForm(forms.ModelForm):
    class Meta:
        model=Albumn
        fields='__all__'
        
        
class ImageForm(forms.ModelForm):
    albumn=forms.CharField(widget=forms.TextInput(attrs={'type':"text",'name':"albumn",'placeholder':"Albumn name"}))
    image=forms.ImageField(widget=forms.FileInput(attrs={'type':"file",'name':"image"}))
    class Meta:
        model=Image
        fields=['image']
        

        


