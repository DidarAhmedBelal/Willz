from django.db import models
from django.conf import settings

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]

    # === Foreign Key to your custom User model (Agency or Company)
    requested_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='service_requests'
    )

    # === Service Details
    service_title = models.CharField(max_length=255)
    service_description = models.TextField()

    # === Contact Info (from user model, duplicated for history tracking)
    agency_name = models.CharField(max_length=100)
    email = models.EmailField()

    # === Status & Rating
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    average_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    total_reviews = models.PositiveIntegerField(default=0)

    # === Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.agency_name} - {self.service_title} ({self.status})"
