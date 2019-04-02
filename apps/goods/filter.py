from django_filters import rest_framework as filters

from .models import Goods

class GoodsFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="shop_price", lookup_expr='gte') #gte 是大于等于的意思
    max_price = filters.NumberFilter(field_name="shop_price", lookup_expr='lte') 
    # name = filters.CharFilter(field_name="name", lookup_expr='icontains')  #contains 模糊查询  i 忽略大小写
    class Meta:
        model = Goods
        fields = ['min_price','max_price']