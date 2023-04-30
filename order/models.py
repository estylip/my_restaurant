from django.db import models
from user.models import User
from django.utils.timezone import now


# Create your models here.
class Cart(models.Model):
        id=models.IntegerField(primary_key=True)
        user=models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
        order=models.OneToOneField(Cart,on_delete=models.CASCADE, primary_key=True)
        is_delivered=models.BooleanField(default=False)
        address=models.CharField(max_length=150)
        comment=models.TextField()
        created=models.DateTimeField(auto_now_add=True)

        