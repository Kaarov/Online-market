from django import template
from shopping.models import *


register = template.Library()


# @register.simple_tag(name='items')
# def get_subcategories():
#     return SubCategory.objects.all()


@register.simple_tag(name='orderitem')
def orderitems(user_id):
    order_check = Order.objects.filter(user_id=user_id, is_draft=True)
    if order_check:
        order = Order.objects.get(user_id=user_id, is_draft=True)
        order_items = OrderItem.objects.filter(order=order)
        return order_items.count()
    return 0


@register.simple_tag(name='wishlistitem')
def wishlistitems(user_id):
    wishes_check = Wishlist.objects.filter(user_id=user_id)
    if wishes_check:
        wishlist = Wishlist.objects.get(user_id=user_id)
        wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)
        return wishlist_items.count()
    return 0


@register.inclusion_tag('shopping/card-wishlist-header.html')
def card_wishlist(user):
    order = Order.objects.get(user=user, is_draft=True)
    order_items = OrderItem.objects.filter(order=order)
    # wishlist = Wishlist.objects.get(user=request)
    # wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)
    return {
        'order_items': order_items,
        # 'wishlist_items': wishlist_items,
    }
