from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer






    




    


