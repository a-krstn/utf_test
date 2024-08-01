from django.urls import path

from . import views


urlpatterns = [
    path('foods/', views.FoodAPIList.as_view(), name='foods'),
]