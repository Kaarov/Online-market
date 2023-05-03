from django.contrib import admin
from .models import *
from django.db.models import QuerySet


admin.site.register(City)
admin.site.register(Brand)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
    list_display_links = ['name', ]
    list_per_page = 5
    search_fields = ['name', ]
    ordering = ['-id', ]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
    list_display_links = ['name', ]
    list_per_page = 5
    search_fields = ['name', ]
    filter = 'active'
    ordering = ['-id', ]
    actions = ['change_active', ]
    list_filter = ['name', 'category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'cur', 'price', 'article', 'active', 'amount', 'brand', 'slug', 'description', 'created']
    list_display_links = ['name', 'cur']
    search_fields = ['name', 'article']
    list_filter = ['name', 'price']
    list_editable = ['amount', 'slug']
    # list_filter = ['sub_category', 'category',
    #                'active']
    list_per_page = 10
    ordering = ['created', ]
    actions = ['change_active_true', 'change_active_false']
    prepopulated_fields = {'slug': ('name', )}

    @admin.action(description='Изменить на Активный')
    def change_active_true(self, request, qs: QuerySet):
        qs.update(active=True)

    @admin.action(description='Изменить на Неактивный')
    def change_active_false(self, request, qs: QuerySet):
        qs.update(active=False)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'user', 'created_at']
    list_display_links = ['name', 'user']
    list_per_page = 5
    search_fields = ['name', ]
    ordering = ['-id', ]


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_draft']
    inlines = [OrderItemAdmin]

    def has_delete_permission(self, request, obj=None):
        return False


class WishlistItemAdmin(admin.TabularInline):
    model = WishlistItem
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [WishlistItemAdmin]

    def has_delete_permission(self, request, obj=None):
        return False
