from django.shortcuts import render
from .models import chatRooms

# Create your views here.

def index(request):
    chatrooms = chatRooms.objects.all()
    context = {
        'chatrooms':chatrooms,    
    }
    return render(request, 'chatapp/index.html', context)
