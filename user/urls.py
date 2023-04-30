from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.login_user, name='login'),
    path('signup/',views.signup, name='signup'),
    path('managerlogin/', views.manager_login, name='manager_login'),
    path('changedetails/<int:id>/', views.change_details,name='change_dt'),
    path('logout/', views.logout_user, name='logout'),
    
]