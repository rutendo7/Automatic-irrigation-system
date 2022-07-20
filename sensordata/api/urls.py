from django.contrib import admin
from django.urls import path

from .views import (
    SensorDataListAPIView,
    SensorDataDeleteAPIView,
    SensorDataDetailAPIView,
    SensorDataUpdateAPIView,
    SensorDataCreateAPIView,
	)

urlpatterns = [
    ##### process flow
    path('results/', SensorDataListAPIView.as_view(), name='list'),
    path('results/new/', SensorDataCreateAPIView.as_view(), name='new'),
    path('results/<int:id>/detail/', SensorDataDetailAPIView.as_view(), name='detail'),
    path('results/<int:id>/edit/', SensorDataUpdateAPIView.as_view(), name='edit'),
    path('results/<int:id>/delete/', SensorDataDeleteAPIView.as_view(), name="delete"),
]
