from django.urls import path, include
from myfirstapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('home/', views.home, name='home'),
    path('random/', views.random, name='random'),
    path('', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()