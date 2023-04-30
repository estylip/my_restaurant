from django.db import models
from order.models import Cart



# Create your models here.
class Category(models.Model):
        id=models.IntegerField(primary_key=True)
        name=models.CharField(max_length=50)
        imageUrl=models.CharField(max_length=200)


class Dish(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField()
    imageUrl=models.CharField(max_length=200)
    is_gloten_free=models.BooleanField(default=False)
    is_vegetarian=models.BooleanField(default=False)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

class Item(models.Model):
       dish=models.ForeignKey(Dish,default="", on_delete=models.CASCADE)
       cart=models.ForeignKey(Cart, default="", on_delete=models.CASCADE)
       amount=models.IntegerField(default=0)





def __str__(self) -> str:
        return self.title
    