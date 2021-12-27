from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

# def home(request):
    # return HttpResponse("Hi from home of pages.") #path herdai home ma ayo vane Hi from home. vanne response dinxa.
def home(request):
    random_num = random.randint(1 , 10)
    context = {
        'random': random_num
    }
    return render(request, 'pages/home.html',  context)

def about(request):
    random_num = random.randint(1 , 10)
    return render(request, 'pages/about.html')

def send(request):
    return render(request, 'pages/send.html')

def receive(request):
    if request.method == 'GET':
        email =  request.GET.get('email')
        #password = request.GET.get('password')
        return HttpResponse(f"HI I AM FROM GET. {email=} ")
    if request.method == 'POST':
        post = request.POST
        email = post.get('email')
        password = post.get('password')
        return HttpResponse(f"hi.I am from post. {email=} {password=}")