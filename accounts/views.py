from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializers import UserSerailizer
from accounts.models import User

# Create your views here.

class AdminRegisterView(APIView):

    def post (self,request):

        form_data = request.data

        serializer =UserSerailizer(data=form_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data

            instance=User.objects.create_superuser(**cleaned_data)

            serializer =UserSerailizer(instance)

            return Response (data=serializer.data)

        else:

            return Response (data=serializer.errors)

class UserRegisterView(APIView):

    def post(self,request):

        form_data = request.data

        serializer =UserSerailizer(data=form_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data

            instance=User.objects.create_user(**cleaned_data)

            serializer = UserSerailizer(instance)

            return Response (data=serializer.data)

        else:

            return Response (data=serializer.errors)

        



