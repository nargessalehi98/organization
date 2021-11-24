from django.http import HttpResponse
from rest_framework import serializers, status
from rest_framework.response import Response

from . import models


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.employee
        fields = ['full_name']


class AssignATaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.task
        fields = ['functor', 'name', 'description', 'organization']


class ApplyForMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RequestForMembership
        fields = ['applicant', 'organization', 'description']


class ApplyForManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RequestForManagement
        fields = ['applicant', 'organization', 'description']


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.task
        fields = ['organization']


class AcceptMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RequestForMembership
        fields = ['applicant', 'organization']


class RemoveMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RequestForMembership
        fields = ['applicant']
