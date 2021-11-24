from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup.as_view(), name='signup'),
    path('assign', views.assign_a_task.as_view(), name='assign'),
    path('membership', views.apply_for_membership.as_view(), name='membership'),
    path('management', views.apply_for_management.as_view(), name='management'),
    path('tasklist', views.task_list.as_view(), name='task_list'),
    path('requestlist', views.request_list.as_view(), name='request_list'),
    path('accept', views.accept_a_request.as_view(), name='accept_request'),
    path('remove', views.remove_an_employee.as_view(), name='remove_an_employee'),
]
