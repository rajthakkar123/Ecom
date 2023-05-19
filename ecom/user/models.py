from django.db import models  
from django.contrib.auth.models import AbstractUser
from django.utils import timezone  
from .managers import CustomUserManager

# Create your models here.  

class CustomUser(AbstractUser):  
    username = None  
    email = models.EmailField(('email_address'), unique=True, max_length = 200)  
    date_joined = models.DateTimeField(default=timezone.now)  
    is_active = models.BooleanField(default=True)  

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []  

    objects = CustomUserManager() 

    def __str__(self):  
        strr = str(self.id)
        return strr

class Address(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Flat_number_society = models.CharField(max_length=255)
    landmark = models.CharField(max_length=50)
    area = models.CharField(max_length=25)
    city = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    
    
    def __str__ (self):
        return self.Flat_number_society + " " + self.landmark + " " + " " + self.area + " " + self.city + " " + self.pincode