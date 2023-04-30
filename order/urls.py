from django.urls import path
from . import views


urlpatterns=[

    path('cart/<int:id>', views.cart, name='cart'),
    path('orderhistory/<int:id>', views.order_history, name='order_history'),
    path('ordermanagment', views.order_managment, name='order_managment'),
    path('order/', views.order, name='order'),
    path('deletedish/<int:id>',views.delete_item, name='delete_item'),
    path('finishorder/',views.finish_order, name='finish_order'),
    
]