from django.urls import path
from .views import test_token
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('token_auth_login/',test_token , name='login'),
    path('token_auth/', obtain_auth_token, name='obtain_token'),
]