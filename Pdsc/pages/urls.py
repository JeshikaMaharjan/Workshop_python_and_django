from django.urls import path
from pages.views import home, about, send, receive

urlpatterns = [
    path('',home),
    path('about/', about),
     #eta 'about/' ma jaile pani about apxi slash halnu
    path('send/', send),
    path('receive/', receive,  name = 'receive'),
    

]