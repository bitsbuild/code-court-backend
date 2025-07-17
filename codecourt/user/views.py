from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from user.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token
@api_view(['POST'])
def create_user(request):
    try:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token,_ = Token.objects.get_or_create(user=user)
        return Response(
            {
                "Status":"Account Created Successfully",
                "Email":request.data['email'],
                "Username":request.data['username'],
                "Token":str(token.key)
            }
        )
    except Exception as e:
        pass
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    try:
        request.user.delete()
        return Response(
            {
                "Status":"Account Deletion Successful"
            }
        )
    except Exception as e:
        return Response(
            {
                "Status":"Error",
                "Error":str(e)
            }
        )
