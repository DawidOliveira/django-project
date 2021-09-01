from api.models import User
from api.serializers import UserSerializer
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

# Create your views here.

class ListUserAPIView(ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class CreateUserAPIView(CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UpdateUserAPIView(UpdateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class DeleteUserAPIView(DestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer