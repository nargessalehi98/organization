from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from .serializers import SignupSerializer, ApplyForMembershipSerializer, \
    AssignATaskSerializer, TaskListSerializer, ApplyForManagementSerializer, AcceptMembershipSerializer, \
    RemoveMembershipSerializer
from . import models
from . import Response


class signup(GenericAPIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            models.employee.objects.create(username=request.user.username,
                                           full_name=serializer.data['full_name'],
                                           organization=" ")
            response = Response.BaseResponse(status.HTTP_200_OK, "Signed up successfully.")
            return HttpResponse(str(response.get_response_body()))
        response = Response.BaseResponse(status.HTTP_400_BAD_REQUEST, "invalid data,try again.")
        return HttpResponse(str(response.get_response_body()))


class apply_for_membership(GenericAPIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated]

    def apply(self, data):
        if models.employee.objects.filter(full_name=data['applicant']).exists():
            return True

    def post(self, request):
        serializer = ApplyForMembershipSerializer(data=request.data)
        if serializer.is_valid():
            if self.apply(serializer.validated_data):
                serializer.save()
                response = Response.BaseResponse(status.HTTP_200_OK, "Request for membership registered.")
                return HttpResponse(str(response.get_response_body()))
        response = Response.BaseResponse(status.HTTP_400_BAD_REQUEST, "invalid data,try again.")
        return HttpResponse(str(response.get_response_body()))


# employee send their request to admin and admin manage them on database
class apply_for_management(GenericAPIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated]

    def apply(self, data, username):
        Employee = models.employee.objects.get(username=username)
        if Employee.organization == data['organization']:
            return True

    def post(self, request):
        serializer = ApplyForManagementSerializer(data=request.data)
        if serializer.is_valid():
            if self.apply(serializer.validated_data, request.user.username):
                serializer.save()
                response = Response.BaseResponse(status.HTTP_200_OK, "Request for management registered.")
                return HttpResponse(str(response.get_response_body()))
        response = Response.BaseResponse(status.HTTP_400_BAD_REQUEST, "You are not employee of this organization.")
        return HttpResponse(str(response.get_response_body()))


class assign_a_task(GenericAPIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated]

    def assign(self, data, username):
        Manager = models.manager.objects.get(username=username)
        Employee = models.employee.objects.get(full_name=data['functor'])
        if Manager.organization == data['organization'] and Employee.organization == data['organization']:
            return True

    def post(self, request):
        serializer = AssignATaskSerializer(data=request.data)
        if serializer.is_valid():
            if self.assign(serializer.validated_data, request.user.username):
                serializer.save()
                response = Response.BaseResponse(status.HTTP_200_OK, "task assigned.")
                return HttpResponse(str(response.get_response_body()))
        response = Response.BaseResponse(status.HTTP_400_BAD_REQUEST, "invalid inoformation.")
        return HttpResponse(str(response.get_response_body()))


class task_list(GenericAPIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TaskListSerializer(data=request.data)
        Manager = models.manager.objects.get(username=request.user.username)
        if serializer.is_valid() and Manager.organization == serializer.data['organization']:
            data = models.task.objects.filter(organization=serializer.data['organization']) \
                .order_by('dead_time')
            response = Response.BaseResponse(status.HTTP_200_OK, str(data))
            return HttpResponse(str(response.get_response_body()))
        return HttpResponse("error", status=400)


class request_list(GenericAPIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if models.manager.objects.filter(username=request.user.username).exists():
            data = models.RequestForMembership.objects.all()
            data = list(data.values())
            response = Response.BaseResponse(status.HTTP_200_OK, data)
            return HttpResponse(str(response.get_response_body()))


class accept_a_request(GenericAPIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated]

    def accept(self, data, username):
        Manager = models.manager.objects.get(username=username)
        if Manager.organization == data['organization']:
            models.employee.objects.filter(full_name=data['applicant']) \
                .update(organization=data['organization'])
            return True

    def post(self, request):
        serializer = AcceptMembershipSerializer(data=request.data)
        if serializer.is_valid():
            if self.accept(serializer.data, request.user.username):
                response = Response.BaseResponse(status.HTTP_200_OK, "request accepted.")
                return HttpResponse(str(response.get_response_body()))
        response = Response.BaseResponse(status.HTTP_400_BAD_REQUEST, "invalid data.")
        return HttpResponse(str(response.get_response_body()))


class remove_an_employee(GenericAPIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated]

    def remove(self, data, username):
        Employee = models.employee.objects.get(full_name=data['applicant'])
        Manager = models.manager.objects.get(username=username)
        if Employee.organization == Manager.organization:
            models.employee.objects.filter(full_name='narges salehi') \
                .update(organization=" ")
            return True

    def put(self, request):
        serializer = RemoveMembershipSerializer(data=request.data)
        if serializer.is_valid():
            if self.remove(serializer.data, request.user.username):
                response = Response.BaseResponse(status.HTTP_200_OK, "employee removed.")
                return HttpResponse(str(response.get_response_body()))
        response = Response.BaseResponse(status.HTTP_200_OK, "invalid data.")
        return HttpResponse(str(response.get_response_body()))
