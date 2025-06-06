from django.urls import path

from . import views

#Here we are mapping show that our logic will get worked and displayed on the website
urlpatterns = [
    
    path('',views.index, name='index')
    
]
