from statistics import mode
from django.utils import timezone
from django.contrib.auth.models import Permission
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from sensordata.models import SensorReading

ALGORITHMS_LIST = (
    ("Decision Tree", "Decision Tree"),
    ("KNearestNeighbour", "KNearestNeighbour"),
    ("NaiveBayes", "NaiveBayes"),
    ("RandomForest", "RandomForest"),
)

irrigationstatus = (
    ("Normal", "Normal"),
    ("Irrigate", "Irrigate"),
   
)


class Prediction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,
                             on_delete=models.CASCADE, blank=True, null=True)
    sensordata = models.ForeignKey(SensorReading, default=1,
                             on_delete=models.CASCADE, blank=True, null=True)
    algorithm = models.CharField(max_length=250, null=True, blank=True)
    status_i  = models.CharField(_("Irrigation status"),max_length=250, choices=irrigationstatus, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.status_i + ' - ' + self.algorithm

    class Meta:
        ordering = ["-timestamp", "-updated"]


class PredictionParameter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,
                             on_delete=models.CASCADE, blank=True, null=True)
    plantname = models.CharField(
        _("Name of the plant"), max_length=250, null=True, blank=True)
    max_temp = models.CharField(
        _("maximum temperature"), max_length=250, null=True, blank=True)
    min_temp = models.CharField(
        _("minimum temperature"), max_length=250, null=True, blank=True)
    max_humidity = models.CharField(
        _("maximum humidity"), max_length=250, null=True, blank=True)
    min_humidity = models.CharField(
        _("minimum humidity"), max_length=250, null=True, blank=True)
    season = models.CharField(
        _("season when crop was planted"), max_length=250, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.plantname

    class Meta:
        ordering = ["-timestamp", "-updated"]
