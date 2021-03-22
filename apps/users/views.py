from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from .models import User, CustomUserManager
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    # queryset = CustomUserManager.objects.all()
    queryset = User.objects.all()
