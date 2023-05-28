from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer


class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by("-id")
    serializer_class = TodoSerializer
