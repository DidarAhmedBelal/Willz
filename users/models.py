from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

def user_profile_upload_path(instance, filename):
    return f"profile_pics/user_{instance.id}/{filename}"

def user_cover_upload_path(instance, filename):
    return f"cover_images/user_{instance.id}/{filename}"

def logo_upload_path(instance, filename):
    return f"logos/user_{instance.id}/{filename}"

class User(AbstractUser):
    ACCOUNT_TYPE_CHOICES = (
        ('Agency', 'Agency'),
        ('Company', 'Company'),
    )

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=15, unique=True, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    account_type = models.CharField(
        max_length=20,
        choices=ACCOUNT_TYPE_CHOICES,
        null=True,
        blank=True
    )

    otp = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    otp_created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    otp_request_count = models.PositiveIntegerField(default=0)
    otp_request_reset_time = models.DateTimeField(blank=True, null=True)

    profile_picture = models.ImageField(upload_to=user_profile_upload_path, blank=True, null=True)
    cover_image = models.ImageField(upload_to=user_cover_upload_path, blank=True, null=True)
    logo_image = models.ImageField(upload_to=logo_upload_path, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
