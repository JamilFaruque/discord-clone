from django.shortcuts import render
from .models import Room
# Create your views here.

rooms = [
    {'id':1,'name':'Learn Python'},
    {'id':2,'name':'Learn Java'},
    {'id':3,'name':'Learn Javascript'},
]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'myapp/home.html',context)

def room(request,pk):

    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'myapp/room.html', context)