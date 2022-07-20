from django.contrib import admin
from . models import Prediction, PredictionParameter

class PredictionModelAdmin(admin.ModelAdmin):
    list_display        = [
                           "user", 
                           "sensordata", 
                           "algorithm", 
                           "status_i",
                           "timestamp",
                           "updated"
                           ]
    list_display_links  = ["updated", "timestamp", "user", "sensordata", "algorithm"]
    list_editable       = ["status_i"]
    list_filter         = ["updated", "timestamp", "algorithm", "user"]
    search_fields       = ["algorithm", "status_i"]
    class Meta:
        model = Prediction
        
class PredictionParameterModelAdmin(admin.ModelAdmin):
    list_display        = [
                           "user", 
                           "plantname",
                           "max_temp",
                           "min_temp",
                           "max_humidity", 
                           "min_humidity", 
                           "season",
                           "timestamp",
                           "updated"
                           ]
    list_display_links  = ["updated", "timestamp", "plantname"]
    list_editable       = ["user"]
    list_filter         = ["updated", "timestamp", "plantname", "season"]
    search_fields       = ["plantname"]
    class Meta:
        model = PredictionParameter

admin.site.register(Prediction, PredictionModelAdmin)
admin.site.register(PredictionParameter, PredictionParameterModelAdmin)
