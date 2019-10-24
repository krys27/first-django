from django.contrib import admin
from .models import Ingredient,Meal,Review

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Meal)
admin.site.register(Review)
