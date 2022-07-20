from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
# from medicine.api.serializers import ProductSerializer
from prediction.models import Prediction, PredictionParameter
# from .serializers import PostSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from django.db import models
from django.conf import settings


class PredictionCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Prediction
        fields = [
        "user", 
        "sensordata", 
        "algorithm", 
        "status_i",
        "timestamp",
        "updated"
        ]


prediction_detail_url = HyperlinkedIdentityField(
        view_name='prediction-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class PredictionDetailSerializer(ModelSerializer):
    url = prediction_detail_url
    class Meta:
        model = Prediction
        fields = [
            'url',
            'id',
            "user", 
            "sensordata", 
            "algorithm", 
            "status_i",
            'updated',
            'timestamp'
        ]

class PredictionListSerializer(ModelSerializer):
    url = prediction_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='prediction-api:delete_parameter',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = Prediction
        fields = [
            'url',
            'id',
            'delete_url',
            "user", 
            "sensordata", 
            "algorithm", 
            "status_i",
            'updated',
            'timestamp'
        ]
        
        

########################################
class PredictionParameterCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = PredictionParameter
        fields = [
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


prediction_parameter_detail_url = HyperlinkedIdentityField(
        view_name='prediction-api:detail_parameter',
        lookup_field='id'#or primary key <pk>
    )

class PredictionParameterDetailSerializer(ModelSerializer):
    url = prediction_parameter_detail_url
    class Meta:
        model = PredictionParameter
        fields = [
            'url',
            'id',
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

class PredictionParameterListSerializer(ModelSerializer):
    url = prediction_parameter_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='prediction-api:delete_parameter',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = PredictionParameter
        fields = [
            'url',
            'id',
            'delete_url',
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
