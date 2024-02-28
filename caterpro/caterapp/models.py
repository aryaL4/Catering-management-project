from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_cater = models.BooleanField(default=False,verbose_name='is_cater')
    is_user = models.BooleanField(default=False,verbose_name='user')
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email

class Catagory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    img = models.ImageField(upload_to='cata_images', blank=True, null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    category = models.ForeignKey('Catagory', on_delete=models.CASCADE,null=True, blank=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name or f"Product-{self.id}"

class Buynow(models.Model):
    category = models.ForeignKey('Catagory', on_delete=models.CASCADE,null=True, blank=True)
    product =models.ForeignKey('Product', on_delete=models.CASCADE)
    username=models.CharField(max_length=50, blank=True, null=True)
    quantity= models.PositiveIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    address=models.TextField()
    finished = models.BooleanField(default=False)