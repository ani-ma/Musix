from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
class RoomView(generics.CreateAPIView):#generics is used for CreateAPIView
    queryset = Room.objects.all() #This class turns the url api/home into JSON data
    serializer_class = RoomSerializer
