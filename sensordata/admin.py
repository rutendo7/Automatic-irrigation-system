from django.contrib import admin
from . models import SensorReading

# Register your models here.
class SensorReadingModelAdmin(admin.ModelAdmin):
    list_display        = [
                           "sensor",
                           "humidity",
                           "temp", 
                           "location", 
                           "latitude",
                           "longitude",
                           "timestamp", 
                           "updated"
                           ]
    list_display_links  = ["updated", "timestamp", "sensor"]
    list_editable       = ["location"]
    list_filter         = ["updated", "timestamp", "sensor"]
    search_fields       = ["sensor"]
    class Meta:
        model = SensorReading
        
admin.site.register(SensorReading, SensorReadingModelAdmin)