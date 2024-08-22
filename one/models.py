from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Albumn(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    albumn=models.CharField(max_length=100)
    created=models.DateField(auto_now_add=True,null=True,blank=True)


    def __str__(self):
        return self.albumn
    
      
class Image(models.Model):
    albumn=models.ForeignKey(Albumn,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media')
    uploaded=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user)
    
    
class Favourites(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image=models.ForeignKey(Image,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.image)
    
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    dob=models.DateField()
    pic=models.ImageField(upload_to='profilepics',null=True,blank=True,default='avatar.png')


    def __str__(self):
        return self.name
    
    
class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=50,blank=True)
    message=models.TextField()
    
    def __str__(self):
        return f'{self.name} about {self.subject}'
       