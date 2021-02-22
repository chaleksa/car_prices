from django.contrib import admin
from .models import VehicleType, Make, Model

# Register your models here.
admin.site.register(VehicleType)
admin.site.register(Make)
admin.site.register(Model)
