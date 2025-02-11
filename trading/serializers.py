from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
from .models import UserProfile

class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    user_type = serializers.ChoiceField(choices=UserProfile.User_Types)

    class Meta:
        model = User
        exclude = ['last_login', 'id', 'groups', 'user_permissions']
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validate_data):
        user_name = self.initial_data.get('username')
        password = self.initial_data.get('password')
        user_type = self.initial_data.get('user_type')

        user = User.objects.create_user(username=user_name, password=password)
        user_profile = UserProfile(user = user, user_type= user_type)

        return user_profile
    
    def get_username(self, obj):
        return obj.user.username

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

