from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.

class User(AbstractUser):
   pass

class Lead(models.Model):
   # SOURCE_CHOICE=(
   #    ("YouTube", "YouTube"),
   #    ("Google", "Google"),
   #    ("Newsletter", "Newsletter"),
   # )

   first_name= models.CharField(max_length=20)
   last_name= models.CharField(max_length=20)
   age= models.IntegerField(default=0)
   created_at= models.DateField(auto_now=True)
   agent= models.ForeignKey('Agent', on_delete=models.CASCADE)

   def __str__(self):
      return f"{self.first_name +' '+ self.last_name}"

   # phoned= models.BooleanField(default=False)
   # source= models.CharField(choices=SOURCE_CHOICE, max_length=100)

class Agent(models.Model):
   user= models.OneToOneField(User, on_delete=models.CASCADE)
   # first_name= models.CharField(max_length=20)
   # last_name= models.CharField(max_length=20)

   def __str__(self) :
      return f"{self.user}"
