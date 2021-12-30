from django.urls import path
from pages.views import home, about, todo, remove_todo

urlpatterns = [
    path('',home),
    path('about/', about),
     #eta 'about/' ma jaile pani about apxi slash halnu
    path ('todo/', todo, name="todo"),
    
    path ('remove-todo/<str:todo>/', remove_todo, name="remove_todo"),

]