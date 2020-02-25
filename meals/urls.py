from django.urls import path,re_path

from . import views
from .views import IngredientView,MealView,MealListView,ReviewView

urlpatterns = [
	path('user/<int:pk>/', views.show_user_home, name='user_home'),	
	path('review/<int:pk>/', ReviewView.as_view(),name='review_detail'),
	path('<int:pk>/write_review/',views.write_review,name='write_review'),
	path('<int:pk>/', MealView.as_view(),name='meal_detail'),
	path('',MealListView.as_view(),name='meal_list'),
	path('ingredient/<int:pk>/', IngredientView.as_view(),name='ingredient_detail'),
        path('ingredients',views.show_index_empty, name='show_index_empty'),
	path('blabla/',views.show_template),
	#path(r'<int:meal_id>/', views.show_index, name='show_index')
]
