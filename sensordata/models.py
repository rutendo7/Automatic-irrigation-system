from statistics import mode
from django.utils import timezone
from django.contrib.auth.models import Permission
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class SensorReading(models.Model):
    sensor     = models.CharField(_("Sensor name"),max_length=250, null=True, blank=True)
    humidity   = models.CharField(_("Humidity value"),max_length=250, null=True, blank=True)
    temp       = models.CharField(_("Temperature value"),max_length=250, null=True, blank=True)
    location   = models.CharField(_("Name of the location"),max_length=250, blank=True, null=True)
    latitude   = models.DecimalField(_("Latitude coordinates"),max_digits=22, decimal_places=16, blank=True, null=True)
    longitude  = models.DecimalField(_("Longitude coordinates"),max_digits=22, decimal_places=16, blank=True, null=True)
    updated    = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp  = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.sensor + ' - ' + self.location

    class Meta:
        ordering = ["-timestamp", "-updated"]
        