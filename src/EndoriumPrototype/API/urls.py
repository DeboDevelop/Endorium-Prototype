from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserAPIView.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]