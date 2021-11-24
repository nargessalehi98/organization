import datetime
from datetime import timedelta
from django.db import models


class organization(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class manager(models.Model):
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class employee(models.Model):
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    organization = models.CharField(max_length=50, default=" ")

    def __str__(self):
        return self.full_name


class task(models.Model):
    functor = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    # each task has a default 10 day deadline
    creation_time = models.DateTimeField(default=datetime.datetime.now() )
    dead_time = models.DateTimeField(default=datetime.datetime.now() + timedelta(days=10))
    organization = models.CharField(default=" ", max_length=50)

    def __str__(self):
        return self.name


# employee send their request to admin and admin manage them on database
class RequestForManagement(models.Model):
    applicant = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class RequestForMembership(models.Model):
    applicant = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
