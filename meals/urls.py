from django.urls import path,re_path

from . import views
from .views import IngredientView,MealView,MealListView

urlpatterns = [
	path('user/<int:pk>/', views.show_user_home, name='show_user_home'),	
	path('<int:pk>/', MealView.as_view(),name='meal_detail'),
	path('',MealListView.as_view(),name='meal_list'),
	path('ingredient/<int:pk>/', IngredientView.as_view(),name='ingredient_detail'),
        path('ingredients',views.show_index_empty, name='show_index_empty'),
	path('blabla/',views.show_template),
	#path(r'<int:meal_id>/', views.show_index, name='show_index')
]
