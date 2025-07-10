from django.contrib import admin

# Register your models here.
from dashboard.models import UserStats, UserOverview, EarningOverview

admin.site.register(UserStats)
admin.site.register(UserOverview)
admin.site.register(EarningOverview)