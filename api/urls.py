from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import (
    UserListView,
    SignupView,
    MyProfileView,
    LoginView,
    SendOTPView,
    VerifyOTPView,
    ChangePasswordView,
    CustomTokenObtainPairView
)

# DRF Router for Admin/UserListView
router = DefaultRouter()
router.register('users', UserListView, basename='user')

urlpatterns = [
    # Router-based (Admin only)
    path('', include(router.urls)),

    # Auth & Profile
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('my-profile/', MyProfileView.as_view(), name='my-profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    # OTP
    path('send-otp/', SendOTPView.as_view(), name='send-otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),

    # JWT Auth
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='jwt-create'),
]
