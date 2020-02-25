from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import DetailView,ListView		
from django.contrib.auth.models import User
from .models import Ingredient,Meal,Review
from .forms import WriteReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

# Create your views here.

class MealView(LoginRequiredMixin,DetailView):
    model = Meal
    template_name = 'meal.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.meal = get_object_or_404(Meal,pk=self.kwargs['pk'])
        context['meal'] = self.meal
        context['review_list'] = Review.objects.filter(meal__id=self.meal.pk)
        return context	
    #login_url = '/login/'
    #redirect_field_name = 'redirect_to'

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

@login_required
def show_user_home(request,pk):
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1
    meals = Meal.objects.filter(host__id=pk)
    meals_r = Meal.objects.filter(guests__id=pk)
    host = User.objects.get(pk=pk)
    context = {'host':host,'meals_hosted':meals,'meals_reviewed':meals_r,'num_visits':num_visits}
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

@login_required
def write_review(request,pk):
    meal = get_object_or_404(Meal,pk=pk)
    if request.method == 'POST':
        form = WriteReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(meal=meal,user=request.id,text=form.cleaned_data['review'])
            #new_review = Review(meal=meal,user=request.id,text=form.cleaned_data['review']
            #meal.guests.add(
	    #new_review.save()

        return HttpResponseRedirect(reverse('meal_detail', args=[str(meal.id)]))

    else:
        proposed_text = 'to be written yet..'
        form = WriteReviewForm(initial={'review':proposed_text})
        context = {'form':form,'meal':meal}
        return render(request,'write_review.html',context)

