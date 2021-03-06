"""vueshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

import xadmin
from vueshop.settings import MEDIA_ROOT
from django.views.static import serve
from goods.views import GoodsListViewsSet

# goods_list =GoodsListViewsSet.as_view({
#     'get':'list'
# })

router = DefaultRouter()
#路由配置
router.register(r'goods',GoodsListViewsSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),  
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'docs/', include_docs_urls(title="慕学生鲜")),#api文档

]
