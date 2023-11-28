from django.db import models

# Create your models here.

class Car(models.Model):
    
    brand = models.CharField(max_length=30)
    color = models.TextField(max_length=15)
    price = models.TextField() 
    image = models.ImageField(upload_to='./static/image/%y/%m/%d')

    def __str__(self) :
        
        return self.brand