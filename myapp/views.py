from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1,'name':'Learn Python'},
    {'id':2,'name':'Learn Java'},
    {'id':3,'name':'Learn Javascript'},
]


def home(request):
    context = {'rooms':rooms}
    return render(request,'myapp/home.html',context)

def room(request,pk):

    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
        context = {'room':room}
    return render(request, 'myapp/room.html', context)