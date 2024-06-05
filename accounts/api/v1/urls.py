from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from accounts.api.v1.views import RegistrationAPIView, LogoutAPIView

urlpatterns = [
        path('register/', RegistrationAPIView.as_view(), name='register'),
        path('logout/', LogoutAPIView.as_view(), name='logout'),
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]