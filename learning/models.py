from django.db import models
from django.db.models.base import Model

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Book(models.Model):
    title=models.CharField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    isbn =models.IntegerField(default=0)
    pages=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    stock=models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    imageurl = models.URLField()
    status=models.BooleanField(default=True)
    date_created=models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag=models.CharField(max_length=10)
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.IntegerField()
    stock=models.IntegerField()
    imageurl = models.URLField()
    status=models.BooleanField(default=True)
    date_created=models.DateField(auto_now_add=True)

    class Meta:
        ordering=['-date_created']
    
    def __str__(self):
        return self.name
    


        

