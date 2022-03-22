from rest_framework import serializers
from .models import DuckModel

class DuckSerializer(serializers.ModelSerializer):
  class Meta:
    fields  = ('id', 'owner','name', 'description', 'species', 'age')
    model   = DuckModel