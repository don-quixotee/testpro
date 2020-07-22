from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# # Create your models here.


class Profile(AbstractUser):
    CHOICES = [('M', 'Male'), ('F', 'Female'), ('None','Other')]
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    image = models.ImageField()
    gender = models.CharField(max_length=50, choices = CHOICES)
    about = models.TextField()
    
    REQUIRED_FIELDS = ('email',)

    def __str__(self):
        return self.username




