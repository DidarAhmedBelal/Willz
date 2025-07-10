from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from services.pagination import ServiceRequestPagination
from services.models import ServiceRequest
from services.serializers import ServiceRequestSerializer

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all().order_by('-created_at')
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ServiceRequestPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status']                     
    search_fields = ['service_title', 'agency_name']   
    ordering_fields = ['created_at', 'average_rating'] 
    ordering = ['-created_at']

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(
            requested_by=user,
            agency_name=user.full_name or user.username,
            email=user.email
        )

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.account_type == "Company":
            return ServiceRequest.objects.all()
        # Agencies see only their own requests
        return ServiceRequest.objects.filter(requested_by=user)

    # === Accept Service ===
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def accept(self, request, pk=None):
        service = self.get_object()
        service.status = 'accepted'
        service.save(update_fields=['status'])
        return Response({'message': 'Service accepted'}, status=status.HTTP_200_OK)

    # === Decline Service ===
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def decline(self, request, pk=None):
        service = self.get_object()
        service.status = 'declined'
        service.save(update_fields=['status'])
        return Response({'message': 'Service declined'}, status=status.HTTP_200_OK)
