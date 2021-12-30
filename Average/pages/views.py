from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    random_num = random.randint(1 , 10)
    context = {
        'random': random_num
    }
    return render(request, 'pages/home.html',  context)

def about(request):
    random_num = random.randint(1 , 10)
    return render(request, 'pages/about.html')

def average(request):
    return render(request, 'pages/average.html')
    

def calc(request):
    if request.method == 'POST':
        num1 =  request.POST.get('first_number')
        num2 =  request.POST.get('second_number')
        num3 = (int(num1) + int(num2)) / 2
        
    return HttpResponse(f"Average is.{num3=}")
    
    


