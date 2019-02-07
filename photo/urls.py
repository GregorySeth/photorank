from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:photo_id>', views.detail, name='detail'),
    path('<int:photo_id>/upvote', views.upvote, name='upvote')
]
