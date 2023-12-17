from pprint import pprint

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from commits.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(min_length=10)

    class Meta:
        model = Comment
        fields = '__all__'

    def validate_user(self, value):
        print('********', value)
        if value.id == 1:
            raise ValidationError('Не допустимое слово')
        return value

    # def validate(self, attrs):
    #     if attrs['user'].id == 1:
    #         raise ValidationError('Вам не разрешено')
    #     pprint(attrs['text'])
    #     return attrs

    def create(self, validates_data):
        print(validates_data)
        return super().create(validates_data)