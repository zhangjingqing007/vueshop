from rest_framework import serializers
from .models import Goods

class GoodsSerializer(serializers.Serializer):
    goods_sn = serializers.CharField(required=True, allow_blank=True, max_length=100)
    name = serializers.CharField(required=True, allow_blank=True, max_length=100)