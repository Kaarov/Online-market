from django.shortcuts import redirect

from shopping.models import *


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def subcategories(request):
    return {
        'subcategories': SubCategory.objects.all()
    }


def products(request):
    return {
        'products': Product.objects.all()
    }


def brands(request):
    return {
        'brands': Brand.objects.all()
    }


def orderitems(request):
    if not request.user.is_authenticated:
        return redirect('home')
    order = Order.objects.get(user=request.user, is_draft=True)
    order_item = OrderItem.objects.filter(order=order)
    return {
        'order_items': order_item
    }


# def wishlistitems(request):
#     if not request.user.is_authenticated:
#         return redirect('home')
#     wishlist = Wishlist.objects.get(user=request.user)
#     wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)
#     return {
#         'wishlist_items': wishlist_items
#     }
