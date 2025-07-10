from rest_framework import serializers
from .models import UserStats, UserOverview, EarningOverview

class UserStatsSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = UserStats
        fields = [
            'user',
            'user_email',
            'total_users',
            'total_earning',
            'last_week_growth_percentage',
            'yesterday_growth_percentage',
            'created_at',
        ]


class UserOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOverview
        fields = [
            'date',
            'user_count',
        ]

class EarningOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EarningOverview
        fields = [
            'month',
            'earning_amount',
        ]
