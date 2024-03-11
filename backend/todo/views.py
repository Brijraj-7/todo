from django.shortcuts import render
from rest_framework import viewsets
from .serializer import todoSerializers
from .models import todo

class todoView(viewsets.ModelViewSet):
    serializer_class = todoSerializers
    queryset = todo.objects.all()