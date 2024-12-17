from rest_framework import generics, viewsets
from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer


#class TaskViewSet(viewsets.ModelViewSet)

class TaskAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer 