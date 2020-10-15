from django.contrib import admin
from django.urls import path, include
from .views import index,galeria,insumos,login,registro,logout_vista

urlpatterns = [
    path('',index,name='INDX'),
    path('galeria/',galeria,name='GALE'),
    path('insumos/',insumos,name='INSUMOS'),
    path('login/',login,name='LOGIN'),
    path('registro/',registro,name='REGIS'),
    path('logout_vista/',logout_vista,name='LOGOUT'),
]