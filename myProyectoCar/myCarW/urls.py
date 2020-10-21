from django.contrib import admin
from django.urls import path, include
from .views import index,galeria,insumos,login,registro,logout_vista,admin_insumos,eliminar,modificar_vista,modificar_insumos

urlpatterns = [
    path('',index,name='INDX'),
    path('galeria/',galeria,name='GALE'),
    path('insumos/',insumos,name='INSUMOS'),
    path('login/',login,name='LOGIN'),
    path('registro/',registro,name='REGIS'),
    path('logout_vista/',logout_vista,name='LOGOUT'),
    path('adm_insumos/',admin_insumos,name='ADM_IN'),
    path('eliminar/<id>/',eliminar,name='ELIMINAR'),
    path('modificar_vista/<id>/',modificar_vista,name='MODIFICAR_V'),
    path('modificar/',modificar_insumos,name='MODIFICAR'),
]