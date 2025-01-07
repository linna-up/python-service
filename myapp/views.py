from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class LoginView(APIView):
    def post(self, request, format=None):
        return Response({
                'msg': 'success',
                'data': '{}',
            }, status=status.HTTP_200_OK)
    
class TestView(APIView):
    def get(self, request, format=None):
        return Response('test', status=status.HTTP_200_OK)