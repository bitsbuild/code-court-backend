from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer,CharField,ValidationError
import re
class UserSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password','confirm_password','email']
        extra_kwargs = {
            "password":{'write_only':True}
        }
    def validate(self, attrs):
        if User.objects.filter(username=attrs['username']).exists():
            raise ValidationError({
                "Status":"Error",
                "Error":"User With This Username Exists"
            })
        elif User.objects.filter(email=attrs['email']).exists():
            raise ValidationError({
                "Status":"Error",
                "Error":"User Exists For This Email ID Exists"
            })
        elif attrs['password'] != attrs['confirm_password']:
            raise ValidationError({
                "Status":"Error",
                "Error":"Passwords Do Not Match"
            })
        else:
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', attrs['email']):
                return attrs
            else:
                raise ValidationError({
                "Status":"Error",
                "Error":"Email ID Of Incorrect Format"
            })
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user