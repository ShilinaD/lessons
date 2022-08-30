from rest_framework import generics
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializer import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        return Response({'title': 'Анджклина Джоли'})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
