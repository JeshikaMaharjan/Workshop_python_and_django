from django.shortcuts import render, redirect
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

# def send(request):
#     return render(request, 'pages/send.html')

# def receive(request):
#     if request.method == 'GET':
#         email =  request.GET.get('email')
#         #password = request.GET.get('password')
#         return HttpResponse(f"HI I AM FROM GET. {email=} ")
#     if request.method == 'POST':
#         post = request.POST
#         email = post.get('email')
#         password = post.get('password')
#         return HttpResponse(f"hi.I am from post. {email=} {password=}")

def get_data():
    with open('data.txt', 'r') as file:
        lines = file.readlines()
    lines = [l.replace('\n', '') for l in  lines] #list comprehension
    return lines

def write_data(text, mode):
    with open('data.txt',mode) as file: #a means append
            file.writelines(str(text) + '\n')
            # print('\n'*10,request.POST.get('text')) #prints in terminal

def clear_data():
    with open('data.txt','w+') as file:
        file.writelines('')

def todo(request):

    if request.method == "POST":
        text = request.POST.get('text')
        write_data(text, 'a+')
               
    data = get_data() #function_call
  
    print(data)

    return render(request, 'pages/todo.html', context = {'data':data})

def remove_todo(request,todo):
    #DELETE
    previous_data = get_data()
    previous_data.remove(todo)
    # print(previous_data)

    clear_data()
    for data in previous_data:
        write_data(data, 'a+')


    return redirect('todo')

    