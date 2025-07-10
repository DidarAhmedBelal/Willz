from rest_framework import serializers
from .models import ServiceRequest
from users.serializers import UserSerializer

class ServiceRequestSerializer(serializers.ModelSerializer):
    requested_by = UserSerializer(read_only=True)  

    class Meta:
        model = ServiceRequest
        fields = [
            'id',
            'requested_by',  
            'agency_name',
            'email',
            'service_title',
            'service_description',
            'status',
            'average_rating',
            'total_reviews',
            'created_at',
        ]
        read_only_fields = ['status', 'average_rating', 'total_reviews', 'created_at']
