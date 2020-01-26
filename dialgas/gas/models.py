from django.db import models
from django.contrib.auth.models import User

class Estate(models.Model):
    estate_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    Admin = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.estate_name

class Supplier(models.Model):
    business_name = models.CharField(max_length=30, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=30)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name

class Consumer(models.Model):
    full_name = models.CharField(max_length=30, unique=False)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=30, unique=True)
    mobile_number = models.CharField(max_length=14, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)


    def __str__(self):
        return self.name.username
