from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    student_id=models.CharField(max_length=20)
    Name=models.CharField(max_length=20)
    dept=models.CharField(max_length=20)
class Food(models.Model):
    title=models.CharField(max_length=150)
    price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    image=models.CharField(max_length=300)


class Restaurant(models.Model):
    name=models.CharField(max_length=70)
    image=models.CharField(max_length=300)
    rating=models.PositiveIntegerField()

class Food2(models.Model):
    title1=models.CharField(max_length=150)
    price1=models.FloatField()
    discount_price1=models.FloatField()
    description1=models.TextField()
    image1=models.CharField(max_length=300)



class Pay(models.Model):
  
  First_name = models.CharField(max_length=100)
  Last_name = models.CharField(max_length=100)
  username = models.CharField(max_length=100,)
  Address = models.TextField()
  Address_2 = models.TextField()
  pincode = models.PositiveIntegerField()
  Name_on_card = models.CharField(max_length=100)
  Credit_card_number = models.PositiveIntegerField()
  Expiration = models.DateField()
  CVV = models.PositiveIntegerField()
#   quantity = models.PositiveIntegerField()
#   title=models.ForeignKey(Food, on_delete=models.CASCADE)


  
