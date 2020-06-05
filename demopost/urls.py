from django.contrib import admin
from django.urls import path, include
from demopost.views import *

app_name = 'suit'

urlpatterns = [
    path('create/', CarCreateView.as_view()),  # car убрал
    path('all/', CarsListView.as_view()),
    #path('car/detail/<int:pk>/', CarDetailView.as_view()),# испитания
]