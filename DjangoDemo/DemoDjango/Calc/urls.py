#In This Code we have to do the mapping of the current app with the url so that
#The user may can call to specific url

from django.urls import path

from . import views

#Here we can use a list of mapping

urlpatterns = [
    
    path('',views.home, name='home'),
    path('add',views.add, name='add'),
    
]