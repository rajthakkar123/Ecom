from django.db import models
from user.models import CustomUser
from django.utils import timezone
from user.models import Address

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255,null=True)    
    
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name= models.CharField(max_length=255,null=True)
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255,null= True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    price = models.IntegerField(default=500)
    discount = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    
    
# class Cart(models.Model):
#     user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=0)
    
    
class Cart(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    
    
class CartItems(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    item_name = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits= 8, decimal_places=2,default=0.00)
    quantity = models.IntegerField(null=True,blank=True)


class Order(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=8,decimal_places=2,default=0.00)
    Address = models.ForeignKey(Address,on_delete=models.CASCADE)


class OrderItems(models.Model):
    product = models.CharField(max_length=50)
    quantity = models.IntegerField()
    main_order = models.ForeignKey(Order,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8,decimal_places=2)  
    