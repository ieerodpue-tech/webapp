from django.urls import path
from . import views
   #Paths del core
    urlpatterns = [
    path('services/', views.services, name="services"),
   
]