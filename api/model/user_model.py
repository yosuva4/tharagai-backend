from django.db import models
from django.contrib.auth.models import User
    
class UserAddress(models.Model):
    ADDRESS_TYPES = (
        ('home', 'Home'),
        ('work', 'Work'),
        ('other', 'Other'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    first_name = models.CharField(max_length=44)
    last_name = models.CharField(max_length=44)
    email  = models.EmailField(unique=True) 
    mobile = models.CharField(max_length=10)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50, default="India") 
    alter_mobile = models.CharField(max_length=10)
    address_type = models.CharField(max_length=10,choices=ADDRESS_TYPES, default='home')

    class Meta:
        verbose_name_plural = "Address"
        
    def __str__(self):
        return f"{self.user}"