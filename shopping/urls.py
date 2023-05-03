from django.conf.urls import url
from django.urls import path, include
from shopping.views import *

# from rest_framework import routers

# app_name = 'shopping'

# router = routers.DefaultRouter()
# router.register(r'category', CategoryViewSet)
# router.register(r'subcategory', SubCategoryViewSet)
# router.register(r'product', ProductListView)

urlpatterns = [

    # path('', include(router.urls)),

    path('', home, name='home'),

    path('account', account, name='account'),

    path('error_404/', error_404, name='error_404'),

    # Brand
    path('brand/<int:b>/', brand, name='brand'),
    path('brand_home/<int:bh>/', brand_home, name='brand_home'),

    # Blog
    # path('blog_list/', blog_list, name='blog_list'),
    # path('blog_single/', blog_single, name='blog_single'),

    # For product
    path('product/', product, name='product'),
    path('product_details/<int:product_id>/', product_details, name='product_details'),
    # path('product_details_edit/<int:product_id>/<int:comment_id>/', product_details_edit,
    # name='product_details_edit'),
    path('product_details_delete/<int:product_id>/<int:comment_id>/', product_details_delete,
         name='product_details_delete'),

    # Wishlist
    path('my_wishlist/', MyWishListView.as_view(), name='my_wishlist'),
    path('add_wishlist/<int:product_id>/', addwishlistview, name='add_wishlist'),
    path('add_wishlist_product/<int:product_id>/', add_wishlist_product_view, name='add_wishlist_product'),
    path('delete_wishlist/<int:product_id>/', delete_wishlist, name='delete_wishlist'),
    path('delete_wishlist_account/<int:product_id>/', delete_wishlist_account, name='delete_wishlist_account'),

    # Cart
    path('my_cart/', MyCartView.as_view(), name='my_cart'),
    path('savecartview/', savecartview, name='savecartview'),
    path('plus_cart/<int:product_id>/', plus_cart, name='plus_cart'),
    path('minus_cart/<int:product_id>/', minus_cart, name='minus_cart'),
    path('delete_cart/<int:product_id>/', delete_cart, name='delete_cart'),
    path('delete_all/', delete_all, name='delete_all'),
    path('add_cart/<int:product_id>/', addcartview, name='add_cart'),
    path('add_cart_product/<int:product_id>/', add_cart_product_view, name='add_cart_product'),
    path('add_cart_product_detail/<int:product_id>/', add_cart_product_detail_view, name='add_cart_product_detail'),

    # Category and subcategory
    path('category_subcategory/<int:cs>/', category_subcategory, name='category_subcategory'),
    path('subcategory_product/<int:product_id>/', subcategory_product, name='subcategory_product'),

    #   ----------

    # API
    # path('product_list_class/', ProductListView.as_view({'get': 'list', 'post': 'create'})),
    # path('product_list_class/<int:id>/', ProductListView.as_view({'get': 'retrieve', 'put': 'update'})),

    # Gmail code
    path('api/v1/send_email/', SentEmailToGmail.as_view({'post': 'create'})),
    path('api/v1/check_email/', LoginCodeView.as_view({'post': 'create'})),
    # path('token/', LoginTokenView.as_view()),
    # path('send/email/', SentEmailToGmail.as_view({'post': 'create'})),
    # path('check/code/', LoginCodeView.as_view({'post': 'create'})),

    # Category API
    path('api/v1/category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/category/<int:id>/', CategoryViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                               'put': 'update', 'delete': 'destroy'})),
    # Subcategory API
    path('api/v1/subcategory/', SubCategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/subcategory/<int:id>/', SubCategoryViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                                     'put': 'update', 'delete': 'destroy'})),

    # Product API
    path('api/v1/product/', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/product/<int:id>/', ProductViewSet.as_view({'get': 'list', 'patch': 'retrieve',
                                                             'put': 'update', 'delete': 'destroy'})),

    #   ----------

]
