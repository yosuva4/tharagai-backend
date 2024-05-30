from django.db import models
import os 
from django.contrib.auth.models import User
from django.utils import timezone


def product_image_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{instance.name.replace(' ', '_')}_image.{ext.lower()}"
    return os.path.join('product_images', new_filename)

class ProductType(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=product_image_path, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productTitle = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to=product_image_path, null=True, blank=True)
    bestSeller = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.product_type.name})"

class ProductVariation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    oldPrice = models.DecimalField(max_digits=10, decimal_places=2,default="0.00")
    
    def __str__(self):
        return f"{self.product.name} - {self.weight} - ₹{self.price}"
    
class Benefits(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    benefit = models.CharField(max_length=300)
    def __str__(self):
        return self.benefit
     
class HowtoUse(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    how_to_use = models.CharField(max_length=300)
    
    def __str__(self):
        return f"{self.how_to_use}"
    
class SkinType(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    skinType = models.CharField(max_length=300)
    
    def __str__(self):
        return f"{self.skinType}"
    
class Ingredients(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredients = models.CharField(max_length=300)
    
    def __str__(self):
        return f"{self.ingredients}"

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductVariation,on_delete=models.CASCADE)
    item_count = models.IntegerField(default=1,null=True)  # Add item_count field with default value
    total_cart = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    isActive = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        self.total_cart = self.item_count * self.product.price
        super().save(*args, **kwargs)  

    def __str__(self):
        return f"{self.user.username}'s Cart"  
    

    