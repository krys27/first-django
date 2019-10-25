from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView,ListView		
from django.contrib.auth.models import User
from .models import Ingredient,Meal,Review

# Create your views here.

class MealView(DetailView):
    model = Meal
    template_name = 'meal.html'

class MealListView(ListView):
    model = Meal
    template_name = 'meal_list.html'

class ReviewView(DetailView):
    model = Review
    template_name = 'review.html'

class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'

class IngredientView(DetailView):
  model = Ingredient
  template_name = 'ingredient.html'

  #def get(self):
  #  return HttpResponse('hello world')

def show_user_home(request,pk):
    meals = Meal.objects.filter(host__id=pk)
    host = User.objects.get(pk=pk)
    context = {'host':host,'meals':meals}
    return render(request,'user.html',context)

def show_index(request,meal_id):
	# return HttpResponse("Hello, {}. You are at the meals index!".format(request.GET.get('name')))
	return HttpResponse("Hello, {}".format(meal_id))
def show_index_empty(request):
	name = request.GET.get('name')
	if name is None: 
	  return HttpResponse("Hello. You are at the meals index!")
	else: 
          return HttpResponse("Hello, {}. You are at the meals index!".format(name))

def show_template(request):
  return render(request,'blabla.html',{})
