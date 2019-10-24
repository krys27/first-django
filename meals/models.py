from django.db import models
  
  
class Ingredient(models.Model):
  title = models.CharField(max_length=255)

def __str__(self):
  return self.title  

class Meta:
  verbose_name = 'Ingredient'
  verbose_name_plural = 'Ingredients'


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
  
