# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Sensor, Measurement
from .serializers import SensorListSerializer, MeasurementAddSerializer, SensorDetailSerializer


class SensorListCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class SensorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementListCreateAPIView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementAddSerializer
