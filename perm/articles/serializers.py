from rest_framework import serializers

from articles.models import Adv


class AdvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = ['id', 'user', 'text', ]
        read_only_fields = ['user', ]
