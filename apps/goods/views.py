from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Goods
from .serializers import GoodsSerializer
from .filter import GoodsFilter

class GoodsPagination(PageNumberPagination):
    #自定义分页
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

#APIView是DRF封装的django的
# class GoodsList(APIView):
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         serializer = GoodsSerializer(goods, many=True)
#         return Response(serializer.data)

#更高级的方式
class GoodsListViewsSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    商品列表页, 分页， 搜索， 过滤， 排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # 繁琐的方式过滤查询
    # def get_queryset(self):
    #     #自定义查询
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get("price_min",0)
    #     if price_min:
    #         queryset = queryset.filter(shop_price__gt = int(price_min))
    #     return queryset

    #drf提供的方式过滤 filter.SearchFilter 搜索
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    #未使用django-filter的方式
    # filterset_fields = ('name', 'shop_price')
    #搜索
    search_fields = ('name','goods_brief')
    #排序
    ordering_fields = ('sold_num', 'shop_price')
    # 使用django-filter
    filter_class = GoodsFilter


    