from django.db import models
from django.contrib.auth.models import User  
  

class Meal(models.Model):
    title = models.CharField(max_length=255)
    host = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_req_host')
    guests = models.ManyToManyField(User,through='Review',related_name='%(app_label)s_%(class)s_req_guests')
    date = models.DateField(auto_now=True)

    def __str__(self):
      return self.title

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    text = models.CharField(max_length=256,blank=True)

    def __str__(self):
        return self.text

class Ingredient(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title  



#class Measure(models.Model):
#  UNIT_CHOICES = (
#	('g','grams'),
#	('ml','milliliters'),
#  )
#  units = models.CharField(max_length=2,choices=UNIT_CHOICES)
#  
#
#class Recipe(models.Model):
#  
#
#class Meal(models.Model):
#  date = models.DateField(auto_now_add=True)
  
