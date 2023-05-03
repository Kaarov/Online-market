# from datetime import datetime

from user.models import User
from django.db import models
from smart_selects.db_fields import ChainedForeignKey


# from django.core.exceptions import ValidationError


# Бренды или Компании
class Brand(models.Model):
    name = models.CharField('Name of Company', max_length=50)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['id']

    def __str__(self):
        return self.name


# Город
class City(models.Model):
    name = models.CharField(max_length=80, verbose_name='City')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = "Cities"
        ordering = ['id']

    def __str__(self):
        return self.name


# Категории. Пример Вода
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    city = models.ManyToManyField(City, verbose_name='City')
    image = models.ImageField(verbose_name='Image', upload_to='category_image/', null=True, blank=True)
    slug = models.SlugField(verbose_name='URL', default='category-', unique=True, db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

    def __str__(self):
        return self.name


#  Под-категория. Пример Газировка
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Category')
    name = models.CharField(max_length=100, verbose_name='Sub Category')
    active = models.BooleanField(verbose_name='Active', default=True)
    image = models.ImageField(verbose_name='Image', upload_to='subcategory_image/')
    slug = models.SlugField(verbose_name='URL', default='subcategory-', unique=True, db_index=True)

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
        ordering = ['id']

    def __str__(self):
        return self.name


# Главный продукт. Пример Кола/Пепси ...
class Product(models.Model):
    currency = [
        ('SOM', 'Сом'),
        ('USD', 'Доллар'),
        ('EURO', 'Евро'),
        ('RUB', 'Рубль'),
    ]
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    subcategory = ChainedForeignKey(SubCategory,
                                    chained_field='category',
                                    chained_model_field='category',
                                    show_all=False,
                                    auto_choose=True,
                                    sort=True,
                                    verbose_name='SubCategory',)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='name')
    slug = models.SlugField(verbose_name='URL', default='product-', unique=True, db_index=True)
    description = models.TextField(verbose_name='description')
    image = models.ImageField(verbose_name='Image', upload_to='product_image/')
    cur = models.CharField(max_length=4, choices=currency, default='SOM', verbose_name='Currency')
    price = models.IntegerField(verbose_name='Price')
    amount = models.PositiveIntegerField(verbose_name='Amount', default=1)
    article = models.IntegerField(verbose_name='Article', unique=True, null=True)
    active = models.BooleanField(verbose_name='Active', default=True)
    created = models.DateField(verbose_name='Date public', auto_now_add=True, blank=True, null=True)
    updated = models.DateField(verbose_name='Date update', auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creater',
                                   related_name='product_creater')

    # user_wishlist = models.ManyToManyField(User, related_name="user_wishlist", blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']

    def __str__(self):
        return '{name} {sub_category}'.format(name=self.name, sub_category=self.subcategory)


# ---------

# ---------
class Xxxxx(models.Model):
    username = models.TextField(verbose_name='Username')
    email = models.TextField(verbose_name='Email')
    password = models.TextField(verbose_name='Password')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'xxxxx'
        verbose_name_plural = 'xxxxx'
        ordering = ['id']

    def __str__(self):
        return self.username
# ---------

# Comment
# ---------


class Comment(models.Model):
    name = models.TextField(verbose_name='Comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['id']

    def __str__(self):
        return self.name


# ---------

# Cart
# ---------


class Order(models.Model):
    ORDER_TYPE = (
        ('cash', 'Нал'),
        ('card', 'Карта'),
        ('odengi', 'О денги'),
    )
    name = models.CharField(max_length=100, default='Order-Product')
    order_type = models.CharField(max_length=40, choices=ORDER_TYPE, null=True)
    user = models.ForeignKey(User, models.CASCADE)
    total_price = models.IntegerField(null=True, blank=True, default=0)
    total = models.IntegerField(null=True, blank=True, default=0)
    amount = models.IntegerField(default=0)
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-id"]

    def __str__(self): 
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    amount = models.IntegerField(default=0)
    total_item_price = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


# ---------

# WishList
# ---------


class Wishlist(models.Model):
    name = models.CharField(max_length=100, default='WishesProduct')
    user = models.ForeignKey(User, models.CASCADE)

    class Meta:
        verbose_name = "WishList"
        verbose_name_plural = "WishLists"
        ordering = ["-id"]

    def __str__(self):
        return self.name


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='wishes')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
