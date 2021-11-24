from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, authentication, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from . import Response


class login_user(APIView):
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = serializers.LoginSerializer(data=data)
        if serializer.is_valid():
            user = authenticate(username=serializer.data['username'],
                                password=serializer.data['password'])
            if user is not None:
                login(request, user)
                response = Response.BaseResponse(status.HTTP_200_OK, "logged in successfully.")
                return HttpResponse(str(response.get_response_body()))
        response = Response.BaseResponse(status.HTTP_404_NOT_FOUND, "Wrong input. ")
        return HttpResponse(str(response.get_response_body()))


class logout_user(APIView):
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        response = Response.BaseResponse(status.HTTP_200_OK, "logged out successfully.")
        return HttpResponse(str(response.get_response_body()))


class register_user(APIView):
    authentication_class = [BasicAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = serializers.LoginSerializer(data=data)
            if serializer.is_valid():
                user = User.objects.create(username=serializer.data['username'])
                user.set_password(serializer.data['password'])
                user.save()
                response = Response.BaseResponse(status.HTTP_200_OK, "registered successfully.")
                return HttpResponse(str(response.get_response_body()))
        except Exception as e:
            print(e)
        response = Response.BaseResponse(status.HTTP_404_NOT_FOUND, "wrong infomartion or already taken.")
        return HttpResponse(str(response.get_response_body()))
