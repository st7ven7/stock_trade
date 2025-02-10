from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView 
from rest_framework.views import status 
from .models import UserProfile, Company, Share, Transaction 
from .serializers import UserCreateSerializer, UserProfileSerializers, CompanySerializers, ShareSerializers, TransactionSerializers

class UserCreateView(APIView):
    def get(self, request, format=None):
        # This could return a message or an empty serializer as an example.
        return Response({"message": "Please send a POST request with your registration details."}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    permission_classes = [permissions.IsAuthenticated]

    def CompanyCreateView(self, serializer):
        user_profile = UserProfile.objects.get(user = self.request.user)

        if user_profile != UserProfile.Company_user:
            return Response({"error":"Only company users can create company"}, status=403)
        serializer.save(company = user_profile)

class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    permission_classes = [permissions.AllowAny]

class ShareCreateView(generics.CreateAPIView):
    queryset = Share.objects.all()
    serializer_class = ShareSerializers
    permission_classes = [permissions.IsAuthenticated]

    def __ShareCreateView(self, serializer):
        user_profile = UserProfile.objects.get(user = self.request.user)
        
        if user_profile != UserProfile.Company_user:
            return Response({"error":"Only company users can create share"}, status=403)
        serializer.save()

class ShareListView(generics.ListAPIView):
    queryset = Share.objects.all()
    serializer_class = ShareSerializers
    permission_classes = [permissions.AllowAny]

class TransactionCreateview(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializers
    permission_classes = [permissions.IsAuthenticated]

    def __TransactionCreateView(self, serializer):
        user_profile = UserProfile.objects.get(user=self.request.user)
        if user_profile != UserProfile.Normal_user:
            return Response({"error":"Only Normal users can buy or sell shares"}, status=403)
        serializer.save(user = self.request.user)

class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializers
    permission_classes = [permissions.IsAuthenticated]

    def __TransactionListView(self, serializer):
        return Transaction.objects.filter(user = self.request.user)
    
