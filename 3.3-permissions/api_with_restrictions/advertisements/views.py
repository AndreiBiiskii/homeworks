from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, Favorite
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer, FavoriteSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filterset_class = AdvertisementFilter
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['status', ]
    # Advertisement.objects.all().delete()

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""

        if self.action in ["create", 'destroy', "update", "partial_update"]:
            return [IsAuthenticated(), IsOwner()]
        return []


class FavoritesViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    # @action(detail=False)
    # def recent_favorites(self, request):
    #     recent_favorites = Favorite.objects.all()
    #     recent_favorites = recent_favorites.get_object_or_404(pk=request.user.id)
    #     print('recent_favorites')
    #     serializer = self.get_serializer(recent_favorites, many=True)
    #     return Response(serializer.data)
