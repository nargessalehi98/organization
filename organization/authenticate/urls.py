from . import views
from django.urls import path

app_name = 'auth'
urlpatterns = [
    path('login', views.login_user.as_view(), name='login'),
    path('logout', views.logout_user.as_view(), name='logout'),
    path('register', views.register_user.as_view(), name='register')
]
