from django.urls import path
from firstapp.views import *

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('create/', book_create, name='book_create'),
    path('update/<int:pk>/', book_update, name='book_update'),
    path('delete/<int:pk>/', book_delete, name='book_delete'),
]