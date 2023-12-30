from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from articles.models import Adv
from articles.permissions import IsOwner
from articles.serializers import AdvSerializer


class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    permission_classes = [IsOwner]
    throttle_classes = [AnonRateThrottle]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
