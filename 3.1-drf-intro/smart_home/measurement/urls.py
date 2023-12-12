from django.conf.urls.static import static
from django.urls import path

from smart_home import settings
from .views import *

urlpatterns = [
                  # TODO: зарегистрируйте необходимые маршруты
                  path('sensors/', SensorListCreateAPIView.as_view()),
                  path('sensor/<int:pk>/', SensorRetrieveUpdateAPIView.as_view()),
                  path('measurements/', MeasurementListCreateAPIView.as_view())
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
