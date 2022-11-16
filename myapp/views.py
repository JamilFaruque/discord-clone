from django.shortcuts import render,redirect
from .models import Room
from .forms import RoomForm
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

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'myapp/create-room.html', context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'myapp/update-room.html',context)


def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method =="POST":
        room.delete()
        return redirect('home')
    context = {'obj':room}
    return render(request,'myapp/delete.html',context)