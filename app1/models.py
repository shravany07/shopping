
import email
from django.db import models

# Create your models here.
class Signup(models.Model):
    First_Name=models.CharField(max_length=12)
    Last_Name=models.CharField(max_length=12)
    email_id=models.EmailField()
    mobile_no=models.PositiveIntegerField()
    password=models.CharField(max_length=8)

    def __str__(self):
        return self.First_Name

class Pro(models.Model):
    name=models.CharField(max_length=50)
    des=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='pro')
    review=models.TextField()
     

class contact_us(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    message=models.TextField()

    def __str__(self):
        return self.email

class fpro(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    img=models.ImageField(upload_to='pro')

    def __str__(self):
        return self.name

    