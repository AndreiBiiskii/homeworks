from django.urls import path

from .views import *

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorListCreateAPIView.as_view()),
    path('sensor/<int:pk>/', SensorRetrieveUpdateAPIView.as_view()),
    path('measurements/', MeasurementListCreateAPIView.as_view())
]
