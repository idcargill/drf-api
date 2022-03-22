from django.urls import path
from django.urls.resolvers import URLPattern

from .views import DuckDetail, DuckModelView
from .serializer import DuckSerializer

urlpatterns = [
  path('', DuckModelView.as_view(), name='duck_view'),
  path('<int:pk>/', DuckDetail.as_view(), name='duck_detail'),
]