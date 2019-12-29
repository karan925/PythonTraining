from django.urls import path
from myfirstapp import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('random/', views.random, name='random'),
]