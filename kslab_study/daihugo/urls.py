from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('templates/', views.index_template, name='index_template'),
]