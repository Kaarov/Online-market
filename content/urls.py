from django.conf.urls import url
from django.urls import path, include
# from rest_framework import routers

from content.views import *

# app_name = 'shopping'

# router = routers.DefaultRouter()
# router.register(r'category', CategoryViewSet)
# router.register(r'subcategory', SubCategoryViewSet)
# router.register(r'createcategory', CategoryCreateViewSet)
# router.register(r'product', ProductListView)


urlpatterns = [

    # path('', include(router.urls)),

    path('blog_list/', blog_list, name='blog_list'),
    path('blog_single/<int:blog_id>', blog_single, name='blog_single'),
]

