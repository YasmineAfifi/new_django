from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=50,error_messages={
        'required':"Name is required",
        'max_length':'The name must be less than 50 char'
        
    })
    email= models.EmailField(unique=True)
    password = models.CharField(max_length=15)

    def __str__(self):

        return self.name
    
    

# class Login(models.Model):
#     username = models.TextField(max_length=50)
#     email = models.EmailField()
    
