from django.shortcuts import render
from rest_framework import generics
from .serializer import DuckSerializer
from .models import DuckModel

class DuckModelView(generics.ListCreateAPIView):
  queryset            = DuckModel.objects.all()
  serializer_class    = DuckSerializer

class DuckDetail(generics.RetrieveDestroyAPIView):
  queryset            = DuckModel.objects.all()
  serializer_class    = DuckSerializer

