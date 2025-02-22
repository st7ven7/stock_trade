from django.urls import path
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserCreateView, CompanyCreateView, CompanyListView, ShareCreateView, ShareListView, TransactionCreateview, TransactionListView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/create/', CompanyCreateView.as_view(), name='company-create'),
    path('shares/', ShareListView.as_view(), name='share-list'),
    path('shares/create/', ShareCreateView.as_view(), name='share-create'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/create/', TransactionCreateview.as_view(), name='transaction-create'),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
