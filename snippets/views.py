from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from snippets import serializers


class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializers = SnippetSerializer(snippets, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializers = SnippetSerializer(snippet)
        return Response(serializers.data)

    def put(self,request, pk, format=None):
        snippet = self.get_object(pk)
        serializers = SnippetSerializer(snippet, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        






    




    


