# from django.contrib.auth.models import User
# from rest_framework import status
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.test import APITestCase, RequestsClient, APIClient
#
#
# class CreateUserTest(APITestCase):
#     authentication_class = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def setUp(self):
#         self.my_admin = User(username='1', is_staff=True, is_superuser=True)
#         self.my_admin.set_password('1')
#         self.my_admin.save()
#         # self.my_admin = User.objects.create_superuser('1', email=None, password='1')
#
#     def test_can_create_user(self):
#         client = APIClient()
#         data = {'username': '1',
#                 'password': '1'}
#         self.my_admin.user_permissions.add(a)
#         response = self.client.login(path='http://0.0.0.0:8081/auth/login', data=data)
#         self.assertEqual(response, status.HTTP_200_OK)
