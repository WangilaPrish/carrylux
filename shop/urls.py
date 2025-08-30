from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
]
