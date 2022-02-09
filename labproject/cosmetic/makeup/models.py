from distutils.archive_util import make_archive
from distutils.command.upload import upload
from operator import mod
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Brand(models.Model):
    """
    Brand for makeup app
    """
    Name = models.CharField(max_length=50)
    Orgin = models.TextField()
    Slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/brands')
    
    def __str__(self) -> str:
        return self.Name
    
    def get_absolute_url():
        pass

class Kind(models.Model):
    """
    Kind for makeup app
    """
    name = models.CharField(max_length=50)
   

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url():
        pass


class Product(models.Model):
    """
    Products for makeup app
    """
    name = models.CharField(max_length=50)
    kind = models.ForeignKey(Kind,on_delete= models.CASCADE)
    descreotion = models.TextField(max_length=100)
    expir_date = models.DateField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    brands = models.ForeignKey(Brand,on_delete= models.CASCADE)
    image = models.ImageField(upload_to='images/products')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url():
        pass

