from django.db import models

# Create your models here.

class User(models.Model):
    user_name=models.CharField(max_length=200, default="")
    password=models.CharField(max_length=5, default=11111)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    is_staff=models.BooleanField(default=False)
    email=models.EmailField()
