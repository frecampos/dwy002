from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
   url(r'^api/insumos/$',views.InsumosViewSet.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)


