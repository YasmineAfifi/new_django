from django.db import models

# Create your models here.

class Car(models.Model):
    
    brand = models.CharField(max_length=30)
    color = models.TextField(max_length=15)
    price = models.DecimalField(max_digits=6,decimal_places=2) 
    image = models.ImageField(upload_to='./static/image/uploaded_image')

    def __str__(self) :
        
        return self.brand