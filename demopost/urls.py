from django.contrib import admin
from django.urls import path, include
from demopost.views import *

app_name = 'demopost'

urlpatterns = [
    path('create/', PostCreateView.as_view()),
    path('all/', PostListView.as_view()),
    path('detail/<int:pk>/', PostDetailView.as_view()),
]