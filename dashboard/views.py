from rest_framework import generics, permissions
from .models import UserStats, UserOverview, EarningOverview
from .serializers import UserStatsSerializer, UserOverviewSerializer, EarningOverviewSerializer


class UserStatsDetailView(generics.RetrieveAPIView):
    serializer_class = UserStatsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return UserStats.objects.get(user=self.request.user)


class UserOverviewListView(generics.ListAPIView):
    queryset = UserOverview.objects.all().order_by('-date')
    serializer_class = UserOverviewSerializer
    permission_classes = [permissions.IsAuthenticated]


class EarningOverviewListView(generics.ListAPIView):
    queryset = EarningOverview.objects.all().order_by('-month')
    serializer_class = EarningOverviewSerializer
    permission_classes = [permissions.IsAuthenticated]
