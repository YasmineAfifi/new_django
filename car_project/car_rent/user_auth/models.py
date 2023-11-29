from django.db import models
from django.core.validators import MinLengthValidator,RegexValidator

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=30,validators=
                            [MinLengthValidator(limit_value=3, message='Name must be more than 3 char'),
                             RegexValidator(regex=r'^[a-zA-Z]+(\s[a-zA-Z]+)?$',message='Name accepts alphabets only')
                            ])
    
    email= models.EmailField(unique=True)
    password = models.CharField(max_length=15,validators=[MinLengthValidator(limit_value=6,message="Password must be between 6 to 15 char")])

    def __str__(self):

        return self.name


