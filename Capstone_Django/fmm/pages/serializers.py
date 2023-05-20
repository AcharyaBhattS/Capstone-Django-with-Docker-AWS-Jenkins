from rest_framework import serializers

from .taggit_serializer import (TagListSerializerField, TaggitSerializer)
from . import models


class FaqSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = models.Faq
        fields = ['id', 'title', 'body', 'status', 'tags']


class MetaDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MetaData
        fields = "__all__"
