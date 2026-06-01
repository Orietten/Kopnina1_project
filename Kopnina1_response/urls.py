from django.urls import path
from . import views

urlpatterns = [
    path('', views.kopnina1_calculator, name='calculator'),
    path('calculator/', views.kopnina1_calculator, name='calculator_full'),
    path('home/', views.kopnina1_home, name='home'),
]