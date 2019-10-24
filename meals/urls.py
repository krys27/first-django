from django.urls import path,re_path

from . import views
from .views import IngredientView,MealView

urlpatterns = [
	path(r'<int:pk>/', MealView.as_view(),name='meal_detail'),
        path('ingredients',views.show_index_empty, name='show_index_empty'),
	path(r'ingredient/<int:pk>/', IngredientView.as_view(),name='ingredient_detail'),
	path(r'blabla/',views.show_template),
	##re_path(r'(P?<pk>\d+)/$', IngredientView.as_view(),name='ingredient_detail')
	#path(r'<int:meal_id>/', views.show_index, name='show_index')
]
