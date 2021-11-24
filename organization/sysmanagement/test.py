from datetime import datetime, timedelta
from unittest import TestCase

from django.utils import timezone

from . import models


class ModelTestCase(TestCase):
    def setUp(self):
        models.organization.objects.create(name="A")
        models.employee.objects.create(username=1,
                                       full_name="narges salehi",
                                       organization="A")
        models.manager.objects.create(username=1,
                                      full_name="sara salehi",
                                      organization=" ")
        models.task.objects.create(functor="narges salehi",
                                   name="daily",
                                   description="daily at 2",
                                   creation_time=datetime.now(),
                                   dead_time=datetime.now() + timedelta(days=10),
                                   organization="A")
        models.RequestForMembership.objects.create(applicant="sara salehi",
                                                   organization="A",
                                                   description="wanna be a member of A")
        models.RequestForMembership.objects.create(applicant="narges salehi",
                                                   organization="B",
                                                   description="wanna be a manager of B")

    def test_organization(self):
        A = models.organization.objects.filter(name="A")
        self.assertEqual(True, A.exists())

    def test_employee(self):
        nargessalehi = models.employee.objects.filter(id=1)
        self.assertEqual(True, nargessalehi.exists())

    def test_manager(self):
        sarasalehi = models.manager.objects.filter(id=1)
        self.assertEqual(True, sarasalehi.exists())

    def test_task(self):
        task1 = models.task.objects.filter(name="daily")
        self.assertEqual(True, task1.exists())

    def test_membership_request(self):
        applicant1 = models.RequestForMembership.objects.filter(applicant="narges salehi")
        self.assertEqual(True, applicant1.exists())

    def test_manager_request(self):
        applicant2 = models.RequestForManagement.objects.filter(applicant="sara salehi")
        self.assertEqual(True, applicant2.exists())