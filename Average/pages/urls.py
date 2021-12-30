from django.urls import path
from os import name
from pages.views import home, about, average, calc

urlpatterns = [
    path('',home),
    path('about/', about),
     #eta 'about/' ma jaile pani about apxi slash halnu
    path('average/', average, name ="average"),
    path('calc/', calc , name ="calc"),
]
    
    
    
