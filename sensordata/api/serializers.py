from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
# from medicine.api.serializers import ProductSerializer 
from sensordata.models import SensorReading
# from .serializers import PostSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from django.db import models
from django.conf import settings


#####Process flow Charts
class SensorDataCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = SensorReading
        fields = [
            'id',
            'sensor',
            'humidity',
            'temp',
            "location", 
            "latitude", 
            "longitude"
        ]


soldstock_detail_url = HyperlinkedIdentityField(
        view_name='sensordata-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class SensorDataDetailSerializer(ModelSerializer):
    url = soldstock_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = SensorReading
        fields = [
            'url',
            'id',
            'user',
            'sensor',
            'humidity',
            'temp',
            "location", 
            "latitude", 
            "longitude",
            'updated',
            'timestamp'
        ]

class SensorDataListSerializer(ModelSerializer):
    url = soldstock_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='sensordata-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = SensorReading
        fields = [
            'url',
            'id',
            'user',
            'delete_url',
            'sensor',
            'humidity',
            'temp',
            "location", 
            "latitude", 
            "longitude",
            'updated',
            'timestamp'
        ]