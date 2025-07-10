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

from dashboard.views import (
    UserOverviewListView,
    EarningOverviewListView,
    UserStatsDetailView
)
from services.views import ServiceRequestViewSet

# DRF Router for Admin/UserListView
router = DefaultRouter()
router.register('users', UserListView, basename='user')
router.register('services', ServiceRequestViewSet, basename='service-request')


urlpatterns = [
    # Router-based (Admin only)
    path('', include(router.urls)),

    # Auth & Profile
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('my-profile/', MyProfileView.as_view(), name='my-profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),


    # Dashboard
    path('stats/me/', UserStatsDetailView.as_view(), name='user-stats-detail'),
    path('overview/users/', UserOverviewListView.as_view(), name='user-overview-list'),
    path('overview/earnings/', EarningOverviewListView.as_view(), name='earning-overview-list'),

    # OTP
    path('send-otp/', SendOTPView.as_view(), name='send-otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),

    # JWT Auth
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='jwt-create'),
]
