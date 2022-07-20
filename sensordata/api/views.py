from rest_framework.generics import ListAPIView

from sensordata.models import SensorReading
# from .serializers import SensorDataSerializer

from django.db.models import Q

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)

from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView, 
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,)

from .pagination import SensorDataLimitOffSetPagination , SensorDataPageNumberPagination

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    SensorDataListSerializer,
    SensorDataDetailSerializer, 
    SensorDataCreateUpdateSerializer,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

#Creating an SensorData
class SensorDataCreateAPIView(CreateAPIView):
    queryset = SensorReading.objects.all()
    serializer_class = SensorDataCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class SensorDataUpdateAPIView(RetrieveUpdateAPIView):
    queryset = SensorReading.objects.all()
    serializer_class = SensorDataCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class SensorDataDeleteAPIView(DestroyAPIView):
    queryset = SensorReading.objects.all()
    serializer_class = SensorDataDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class SensorDataDetailAPIView(RetrieveAPIView):
    queryset = SensorReading.objects.all()
    serializer_class = SensorDataDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class SensorDataListAPIView(ListAPIView):
    serializer_class = SensorDataListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    # pagination_class = SensorDataPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = SensorReading.objects.filter()
        id = self.request.query_params.get('sensor', None)
        if id is not None:
            queryset = queryset.filter(sensor=id)
            print("hey you", queryset)
        return queryset


class SensorDataUserListAPIView(ListAPIView):
    serializer_class = SensorDataListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['sensor']
    # pagination_class = SensorDataPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = SensorReading.objects.filter()
        id = self.request.query_params.get('location', None)
        if id is not None:
            queryset = queryset.filter(location=id)
            print("hey you", queryset)
        return queryset