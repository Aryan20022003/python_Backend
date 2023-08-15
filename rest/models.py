from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.
class Company(models.Model):
    Company_id = models.AutoField(primary_key=True)
    Company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=50, default="Bangalore")
    about = models.TextField()
    type = (("IT", "IT"), ("Non-IT", "Non-IT"))
    Company_type = models.CharField(max_length=15, choices=type, default="IT")

    def __str__(self):
        return self.Company_name


# create model to store tokens for each user

# class tokenDb(models.Model):
#     userId=models.CharField(max_length=100)
#     tokens=ArrayField(models.CharField(max_length=100),size=5)

#     def __str__(self):
#         return self.userId

# create a user data model contain name and password and rating


class userData(models.Model):
    userId = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.userId

    def set_password(self, password):
        self.password = make_password(password)
        self.save()

    def check_password(self, password):
        return check_password(password, self.password)
