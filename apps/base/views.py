from django.shortcuts import render
from rest_framework import generics
from apps.base.models import Women
from apps.base.serializers import WomenSerializers

class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers




# Create your views here.
