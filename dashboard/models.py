from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_users = models.PositiveIntegerField(default=0)
    total_earning = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    last_week_growth_percentage = models.FloatField(default=0)
    yesterday_growth_percentage = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Stats for {self.user.email}"


class UserOverview(models.Model):
    date = models.DateField()
    user_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"User Overview {self.date} - {self.user_count}"


class EarningOverview(models.Model):
    month = models.DateField() 
    earning_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Earnings for {self.month.strftime('%b %Y')}: {self.earning_amount}"
