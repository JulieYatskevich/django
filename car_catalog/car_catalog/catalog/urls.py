from django.urls import path

from . import views


urlpatterns = [
   path('', views.index, name='main'),
   path('main', views.index, name='main'),
   path('brand', views.brand, name='brand'),
   path('add-motor', views.add_motor, name='add-motor'),
   path('add-car', views.add_car, name='add-car'),
   path('catalog', views.catalog, name='catalog'),
]
