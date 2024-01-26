from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request  # new
from rest_framework.response import Response  # new
from rest_framework import status  # new
from rest_framework.decorators import api_view  # new *
from rest_framework.views import APIView  # new *
from rest_framework import generics, mixins  # new *
from rest_framework import viewsets  # new * new
from .models import Todo
from .serializer import TodoSerializer


# class TodosGenericApiView(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# class TodosGenericDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

class TodosViewSetApiView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
