from django.urls import path
from . import views
urlpatterns = [

   #Paths del core
  path('contact/', views.contact, name="contact"),
   
]