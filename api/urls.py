from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import (
    UserList,
    SignupView,
    MyProfileView,
    LoginView,
    SendOTPView,
    VerifyOTPView,
    ChangePasswordView,
    CustomTokenObtainPairView
)

router = DefaultRouter()
router.register('users', UserList)

urlpatterns = [

    path('', include(router.urls)),

    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('my-profile/', MyProfileView.as_view(), name='my-profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    path('send-otp/', SendOTPView.as_view(), name='send-otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),

    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='jwt-create'),
]