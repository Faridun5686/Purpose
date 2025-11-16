from rest_framework import serializers
from .models import UserModel
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'password', 'password2', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
        }
    

    # Email validatsiyasi
    def validate_email(self, value):
        validate_email(value)
        if UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError("Bu email allaqachon mavjud.")
        return value
    



    # Parollarni solishtirish
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Parollar mos emas")
        validate_password(attrs['password'])
        return attrs
  
    # Yangi foydalanuvchi yaratish
    def create(self, validated_data):
        validated_data.pop('password2')
        user = UserModel(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
