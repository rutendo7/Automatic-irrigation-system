from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class SensorDataLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10

class SensorDataPageNumberPagination(PageNumberPagination):
    page_size = 10