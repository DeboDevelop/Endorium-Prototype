from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserAPIView.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('adminmaps/', AdminMapAPIView.as_view()),
    path('adminmaps/<int:pk>/', AdminMapDetail.as_view()),
    path('messages/', MessageAPIView.as_view()),
    path('messages/<int:pk>/', MessageDetail.as_view()),
]