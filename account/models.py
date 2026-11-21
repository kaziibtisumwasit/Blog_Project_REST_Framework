from django.db import models
from django.contrib.auth.models import AbstractUser  

# Create your models here.


class CustomUser(AbstractUser):
    # Add any additional fields you want for your custom user model
    
    USER_TYPE_CHOICES = ( 
    ('admin', 'Admin'),
    ('editor', 'Editor'),
    ('guest', 'Guest User'),
    
    
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='guest')