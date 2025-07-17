from django.urls import path
from user.views import create_user,delete_user
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('create/',create_user,name='create'),
    path('delete/',delete_user,name='delete'),
    path('gettoken/',obtain_auth_token,name='gettoken')
]