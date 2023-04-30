from django.urls import path
from . import views



urlpatterns=[
    path('all_categories/', views.all_categories, name='all_categories'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:id>', views.edit_category, name='edit_category'),
    path('delete_category/<int:id>', views.delete_category, name='delete_category'),
    path('all_dishes/', views.all_dishes, name='all_dishes'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('edit_dish/<int:id>', views.edit_dish, name='edit_dish'),
    path('delete_dish/<int:id>', views.delete_dish,name='delete_dish'),
    path('menu/', views.show_menu, name='menu'),
    path('dish_categories/<int:id>', views.dish_by_category ,name='dish_categories')


]