from rest_framework import serializers

from shopping.models import *


# ----------

# Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


# Category/Subcategory
class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField('get_sub_categories')

    class Meta:
        model = Category
        fields = ['id', 'name', 'city', 'image', 'sub_categories']

    def get_sub_categories(self, obj):
        sub_categories = SubCategory.objects.filter(category=obj)
        return SubcategorySerializer(sub_categories, many=True).data


# Category with Subcategory
# class SubCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubCategory
#         fields = ['id', 'name', 'image']
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     sub_categories = serializers.SerializerMethodField('get_sub_categories')
#
#     class Meta:
#         model = Category
#         fields = ['name', 'city', 'image', 'sub_categories']
#
#     def get_sub_categories(self, obj):
#         sub_categories = SubCategory.objects.filter(category=obj)
#         return SubCategorySerializer(sub_categories, many=True).data


# ----------

# Subcategory
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class Product_Sub(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SubCategoryDetailSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField('get_products')

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug', 'active', 'image', 'products']

    def get_products(self, obj):
        products = Product.objects.filter(subcategory=obj)
        return Product_Sub(products, many=True).data


# ----------

# Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
