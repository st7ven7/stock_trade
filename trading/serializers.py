from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
from .models import UserProfile

class UserCreateSerializer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(choices=UserProfile.User_Types)

    class Meta:
        model = User
        fields = ['username', 'password', 'user_type']
        extra_kwargs = {'password':{'write_only': True}}

        def post(self, validate_data):
            user_type = validate_data.pop('user_type')
            user = User.objects.create_user(**validate_data)
            UserProfile.objects.create(user = user, user_type= user_type)
            return user

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

class ShareSerializers(serializers.ModelSerializer):

    company = CompanySerializers(read_only = True)
    class Meta:
        model = models.Share
        fields = '__all__'

class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = '__all__'

