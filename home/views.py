from django.shortcuts import render
from .models import HomeSearch
from .serializers import LeadSerializer
from rest_framework import generics


class HomeSearchCreate(generics.ListCreateAPIView):
    queryset = HomeSearch.objects.all()
    serializer_class = LeadSerializer
