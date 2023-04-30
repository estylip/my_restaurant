
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/',include('main.urls')),
    path('restaurant/user/', include('user.urls')),
    path('restaurant/menu/', include('menu.urls')),
    path('restaurant/order/', include('order.urls'))
]
