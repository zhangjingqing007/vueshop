from rest_framework import serializers
from .models import Goods,GoodsCategory

class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =GoodsCategory
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    #自定义字段,必须和goods里面的字段一致
    category = GoodsCategorySerializer()
    class Meta:
        model =Goods
        fields = "__all__"
        # fields = ('id','category','goods_sn','name','sold_num','fav_num','goods_num','market_price','shop_price','goods_front_image','is_new','is_hot','add_time',)