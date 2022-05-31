from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LegendsSerializer
from .models import Legend

# Create your views here.

class LegendView(viewsets.ModelViewSet):
    serializer_class = LegendsSerializer
    queryset = Legend.objects.all()
