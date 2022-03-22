from django.shortcuts import render
from rest_framework import generics
from .serializer import DuckSerializer
from .models import DuckModel
from ducks.permissions import IsOwnerOrReadOnly

class DuckModelView(generics.ListCreateAPIView):
  permission_classes  = (IsOwnerOrReadOnly,)
  queryset            = DuckModel.objects.all()
  serializer_class    = DuckSerializer

class DuckDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes  = (IsOwnerOrReadOnly,)
  queryset            = DuckModel.objects.all()
  serializer_class    = DuckSerializer

