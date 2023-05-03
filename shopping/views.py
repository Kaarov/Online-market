from datetime import datetime
from time import timezone

from django.core.mail import send_mail
import random

from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

import requests  # for tb bot which will send report to group
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from MilkyWay import settings
from user.permissions import *

from .models import *
from .serializers import *

from shopping.models import *

from user.models import User


def home(request):
    category = Category.objects.all().order_by('name')
    subcategory = SubCategory.objects.all().order_by('name')
    product = Product.objects.all().order_by('name')
    product_last_3 = Product.objects.order_by('created')[:4]
    product_4 = Product.objects.order_by('name')[:9]
    brand = Brand.objects.all().order_by('name')
    context = {
        'product': product,
        'category': category,
        'subcategory': subcategory,
        'product_last_3': product_last_3,
        'brand': brand,
        'product_4': product_4
    }
    return render(request, 'shopping/home.html', context=context)


def account(request):
    if not request.user.is_authenticated:
        return redirect('home')
    wishlist = Wishlist.objects.filter(user=request.user).first()
    wishlist_item = WishlistItem.objects.order_by('id').filter(wishlist=wishlist)
    order_check = Order()
    if order_check.is_draft:
        order = Order.objects.filter(user=request.user, is_draft=False)
        context = {
            'wishlist': wishlist,
            'wishlist_item': wishlist_item,
            'order': order,
        }
    else:
        context = {
            'wishlist': wishlist,
            'wishlist_item': wishlist_item,
        }
    return render(request, 'user/account.html', context=context)


def error_404(request):
    return render(request, 'user/404.html')


# def blog_list(request):
#     return render(request, 'blog/blog.html')
#
#
# def blog_single(request):
#     return render(request, 'blog/blog-single.html')


# def contact(request):
#     if not request.user.is_authenticated:
#         return redirect('home')
#     return render(request, 'user/contact.html')


# ---------

# Brand
def brand(request, b):
    if not request.user.is_authenticated:
        return redirect('home')
    category = Category.objects.all().order_by('name')
    subcategory = SubCategory.objects.all().order_by('name')
    brand_product = Brand.objects.get(id=b)
    product = Product.objects.filter(brand_id=brand_product).order_by('name')
    brand = Brand.objects.all().order_by('name')
    context = {
        'product': product,
        'category': category,
        'subcategory': subcategory,
        'brand': brand,
    }
    return render(request, 'shopping/brand.html', context=context)


def brand_home(request, bh):
    if not request.user.is_authenticated:
        return redirect('home')
    category = Category.objects.all().order_by('name')
    subcategory = SubCategory.objects.all().order_by('name')
    brand_product = Brand.objects.get(id=bh)
    product = Product.objects.filter(brand_id=brand_product).order_by('name')
    brand = Brand.objects.all().order_by('name')
    product_last_3 = Product.objects.order_by('created')[:4]
    context = {
        'product': product,
        'category': category,
        'subcategory': subcategory,
        'product_last_3': product_last_3,
        'brand': brand,
    }
    return render(request, 'shopping/brand_home.html', context=context)


# ---------

# Product

# ---------


def category_subcategory(request, cs):
    if not request.user.is_authenticated:
        return redirect('home')
    category_subcategory = SubCategory.objects.all().order_by('name').filter(category__id=cs)
    subcategory = Category.objects.get(id=cs)
    return render(request, 'shopping/category_subcategory.html', context={
        'category_subcategory': category_subcategory,
        'subcategory': subcategory,
    })


def subcategory_product(request, product_id):
    if not request.user.is_authenticated:
        return redirect('home')
    subcategory_product = Product.objects.all().order_by('name').filter(subcategory_id=product_id)
    category = Category.objects.all().order_by('name')
    subcategory = SubCategory.objects.all().order_by('name')
    brand = Brand.objects.all().order_by('name')
    way = SubCategory.objects.get(id=product_id)

    page = request.GET.get('page', 1)

    paginator = Paginator(subcategory_product, 12)
    try:
        subcategory_product = paginator.page(page)
    except PageNotAnInteger:
        subcategory_product = paginator.page(1)
    except EmptyPage:
        subcategory_product = paginator.page(paginator.num_pages)

    context = {
        'subcategory_product': subcategory_product,
        'category': category,
        'subcategory': subcategory,
        'brand': brand,
        'way': way,
    }
    return render(request, 'shopping/subcategory_product.html', context=context)


def product(request):
    if not request.user.is_authenticated:
        return redirect('home')
    category = Category.objects.all().order_by('name')
    subcategory = SubCategory.objects.all().order_by('name')
    product = Product.objects.all().order_by('name')
    brand = Brand.objects.all().order_by('name')

    page = request.GET.get('page', 1)

    paginator = Paginator(product, 12)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)

    context = {
        'product': product,
        'category': category,
        'subcategory': subcategory,
        'brand': brand,
    }
    return render(request, 'shopping/products.html', context=context)


def product_details(request, product_id):
    if not request.user.is_authenticated:
        return redirect('home')
    product = Product.objects.get(pk=product_id)
    context = {
        'product': product,
    }
    if request.method == 'POST':
        if 'add_comment' in request.POST:
            name = request.POST['comment']
            comment = Comment(
                name=name,
                product=product,
                user=request.user
            )
            comment.save()
            return redirect('product_details', product_id=product_id)
    return render(request, 'shopping/product_details.html', context=context)


# def product_details_edit(request, product_id, comment_id):
#     product = Product.objects.get(pk=product_id)
#     private_product_comment = Comment.objects.get(product=product, pk=comment_id)
#     context = {
#         'product': product,
#         'private_product_comment': private_product_comment,
#     }
#     if request.method == 'POST':
#         if 'add_comment' in request.POST:
#             name = request.POST['name']
#             private_product_comment.name = name
#             private_product_comment.save()
#             return redirect('product_details', product_id=product_id)
#     return render(request, 'shopping/product_details.html', context=context)


def product_details_delete(request, product_id, comment_id):
    if not request.user.is_authenticated:
        return redirect('home')
    product = Product.objects.get(pk=product_id)
    private_product_comment = Comment.objects.get(product=product, pk=comment_id)
    private_product_comment.delete()
    return redirect('product_details', product_id)


# ---------

# End Product

# Wishlist
# ----------

class MyWishListView(TemplateView):
    template_name = 'cart/wishlist.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        wishlist = Wishlist.objects.filter(user=request.user).first()
        wishlist_item = WishlistItem.objects.order_by('id').filter(wishlist=wishlist)
        return render(request, self.template_name, {'wishlist': wishlist, 'wishlist_item': wishlist_item})


def addwishlistview(request, product_id):
    if not request.user.is_authenticated:
        return redirect('home')
    wishlist, is_wishlist_created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_item, is_wishlist_item_created = WishlistItem.objects.get_or_create(product_id=product_id,
                                                                                 wishlist_id=wishlist.id)

    if is_wishlist_created or is_wishlist_item_created:
        wishlist_item.wishlist = wishlist
    else:
        wishlist_item.wishlist = wishlist
    wishlist_item.save()
    wishlist.save()
    return redirect('home')


def add_wishlist_product_view(request, product_id):
    if not request.user.is_authenticated:
        return redirect('home')
    wishlist, is_wishlist_created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_item, is_wishlist_item_created = WishlistItem.objects.get_or_create(product_id=product_id,
                                                                                 wishlist_id=wishlist.id)

    if is_wishlist_created or is_wishlist_item_created:
        wishlist_item.wishlist = wishlist
    else:
        wishlist_item.wishlist = wishlist
    wishlist_item.save()
    wishlist.save()
    return redirect('product')


def delete_wishlist(request, product_id):
    order_item = WishlistItem.objects.get(wishlist__user=request.user, product_id=product_id)
    order_item.delete()
    return redirect('my_wishlist')


def delete_wishlist_account(request, product_id):
    order_item = WishlistItem.objects.get(wishlist__user=request.user, product_id=product_id)
    order_item.delete()
    return redirect('account')


# ---------

# End Wishlist

# Cart

# ---------


def send_message_to_telegram_group(text):
    token = "5363003492:AAGTG7G7fD5DyY8iAEYkXH-YxVxhd6bnht0"
    chat_id = "-796850697"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    # results = requests.get(url_req)


def plus_cart(request, product_id):
    order = Order.objects.get(user=request.user, is_draft=True)
    order_item = OrderItem.objects.get(product_id=product_id, order=order)
    order_item.amount += 1
    order_item.total_item_price += order_item.product.price
    order.total_price = order.total_price + order_item.product.price
    order.total = order.total + order_item.product.price
    order_item.save()
    order.save()
    return redirect('my_cart')


def minus_cart(request, product_id):
    order = Order.objects.get(user=request.user, is_draft=True)
    order_item = OrderItem.objects.get(product_id=product_id, order=order)
    if order_item.amount == 1:
        return redirect('delete_cart', product_id)
    order_item.amount -= 1
    order_item.total_item_price -= order_item.product.price
    order.total_price = order.total_price - order_item.product.price
    order.total = order.total - order_item.product.price
    order_item.save()
    order.save()
    return redirect('my_cart')


def delete_cart(request, product_id):
    order = Order.objects.get(user=request.user, is_draft=True)
    order_item = OrderItem.objects.get(product_id=product_id, order=order)
    order_item_amount = order_item.amount
    order_item_total_item_price = order_item.total_item_price
    # order_total_price = order.total_price
    # order_total = order.total
    order_item.save()
    order_item.delete()
    order.total_price = order.total_price - order_item_total_item_price
    order.total = order.total - order_item_total_item_price - 5
    order.save()
    return redirect('my_cart')


def delete_all(request):
    order = Order.objects.get(user=request.user, is_draft=True)
    if order.items:
        delete = order.items.all()
        for x in delete:
            x.save()
            x.delete()
    order.total_price = 0
    order.total = 0
    order.save()
    return redirect('my_cart')


class MyCartView(TemplateView):
    template_name = 'cart/cart.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        order = Order.objects.filter(user=request.user, is_draft=True).first()
        order_item = OrderItem.objects.order_by('id').filter(order=order)
        return render(request, self.template_name, {'order': order, 'order_item': order_item})


def addcartview(request, product_id):
    if not request.user.is_authenticated:
        return redirect('home')
    order, is_order_created = Order.objects.get_or_create(user=request.user, is_draft=True)
    order_item, is_orderitem_created = OrderItem.objects.get_or_create(product_id=product_id, order_id=order.id)

    if is_order_created or is_orderitem_created:
        order_item.amount = 1
        order_item.order = order
        order_item.total_item_price = order_item.product.price
        order.total_price = order.total_price + order_item.total_item_price
        order.total = order.total + order_item.total_item_price + 5
    else:
        order_item.amount += 1
        order_item.order = order
        order_item.total_item_price += order_item.product.price
        order.total_price = order.total_price + order_item.product.price
        order.total = order.total + order_item.product.price
    order_item.save()
    order.save()
    return redirect('home')


def add_cart_product_view(request, product_id):
    if not request.user.is_authenticated:
        return redirect('home')
    order, is_order_created = Order.objects.get_or_create(user=request.user, is_draft=True)
    order_item, is_orderitem_created = OrderItem.objects.get_or_create(product_id=product_id, order_id=order.id)

    if is_order_created or is_orderitem_created:
        order_item.amount = 1
        order_item.order = order
        order_item.total_item_price = order_item.product.price
        order.total_price = order.total_price + order_item.total_item_price
        order.total = order.total + order_item.total_item_price + 5
    else:
        order_item.amount += 1
        order_item.order = order
        order_item.total_item_price += order_item.product.price
        order.total_price = order.total_price + order_item.product.price
        order.total = order.total + order_item.product.price
    order_item.save()
    order.save()
    return redirect('product')


def add_cart_product_detail_view(request, product_id):
    if not request.user.is_authenticated:
        return redirect('home')
    order, is_order_created = Order.objects.get_or_create(user=request.user, is_draft=True)
    order_item, is_orderitem_created = OrderItem.objects.get_or_create(product_id=product_id, order_id=order.id)

    if is_order_created or is_orderitem_created:
        order_item.amount = 1
        order_item.order = order
        order_item.total_item_price = order_item.product.price
        order.total_price = order.total_price + order_item.total_item_price
        order.total = order.total + order_item.total_item_price + 5
    else:
        order_item.amount += 1
        order_item.order = order
        order_item.total_item_price += order_item.product.price
        order.total_price = order.total_price + order_item.product.price
        order.total = order.total + order_item.product.price
    order_item.save()
    order.save()
    return redirect('product_details', product_id)


def savecartview(request):
    if not request.user.is_authenticated:
        return redirect('home')
    order_check = Order()
    if order_check.is_draft:
        order = Order.objects.get(user=request.user, is_draft=True)
        order_item = OrderItem.objects.filter(order=order)

        for x in order.items.all():
            order.amount += 1

        order.name = f'Order Done {order.id} : {request.user.username}'

        text = f'Order : {order.id}\n'

        for x in range(len(order_item)):
            text += f'{order_item[x].amount}  X  {order_item[x].product.name}({order_item[x].product.price}$)' \
                    f'       {order_item[x].total_item_price}$\n'
        text += '-----------------------------------\n'
        text += f'Total : {order.total_price}\n'
        text += f'TotalPrice : {order.total}\n'
        text += '-----------------------------------\n'
        text += f'Client : {request.user.username}\n'
        text += f'OrderType : {order.order_type}\n'
        send_message_to_telegram_group(text)

        order.is_draft = False
        order.save()
        return redirect('my_cart')
    return redirect('home')


# send_mail(
#         subject='Subject',
#         message='Message',
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=['footstyle10r@gmail.com']
#     )


# End Cart

# ---------


#


# Rest Api


# ---------

# Category
class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve', 'create', 'update']:
            self.permission_classes = [IsAuthenticated & VIPPermission | ManagerPermission]
        else:
            self.permission_classes = [IsAuthenticated & ManagerPermission]
        return super(CategoryViewSet, self).get_permissions()

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         self.serializer_class = CategoryDetailSerializer
    #     else:
    #         self.serializer_class = CategorySerializer
    #     return super(CategoryViewSet, self).get_serializer_class()

    def list(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        check = Category.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Category.objects.get(pk=kwargs.get('id'))
            serializer = CategoryDetailSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        check = Category.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Category.objects.get(pk=kwargs.get('id'))
            serializer = CategorySerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        check = Category.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Category.objects.get(pk=kwargs.get('id'))
            self.perform_destroy(instance)
        else:
            return Response("error: Not found", status=200)
        return Response("success: Destroyed", status=200)


# ---------

# Subcategory
class SubCategoryViewSet(ModelViewSet):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve', 'create', 'update']:
            self.permission_classes = [IsAuthenticated & VIPPermission | ManagerPermission]
        else:
            self.permission_classes = [IsAuthenticated & ManagerPermission]
        return super(SubCategoryViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = SubCategory.objects.all()
        serializer = SubCategorySerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        check = SubCategory.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = SubCategory.objects.get(pk=kwargs.get('id'))
            serializer = SubCategoryDetailSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        check = SubCategory.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = SubCategory.objects.get(pk=kwargs.get('id'))
            serializer = SubCategorySerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        check = SubCategory.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = SubCategory.objects.get(pk=kwargs.get('id'))
            self.perform_destroy(instance)
        else:
            return Response("error: Not found", status=200)
        return Response("success: Destroyed", status=200)


# ---------

# Product
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve', 'create', 'update']:
            self.permission_classes = [IsAuthenticated & VIPPermission | ManagerPermission]
        else:
            self.permission_classes = [IsAuthenticated & ManagerPermission]
        return super(ProductViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        check = Product.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Product.objects.get(pk=kwargs.get('id'))
            serializer = ProductSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        check = Product.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Product.objects.get(pk=kwargs.get('id'))
            serializer = ProductSerializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response("error: Not found", status=200)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        check = Product.objects.filter(pk=kwargs.get('id'))
        if check:
            instance = Product.objects.get(pk=kwargs.get('id'))
            self.perform_destroy(instance)
        else:
            return Response("error: Not found", status=200)
        return Response("success: Destroyed", status=200)


# Check Email Password from Gmail
class SentEmailToGmail(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data['name']
        email = request.data['email']
        code = str(random.randint(1000, 9999))
        now = datetime.now()

        user = User.objects.filter(username=username)
        if user:
            user = user[0]
            if user.attempt <= 4:
                if len(email) > 0:
                    receiver_address = email
                    mail_content = f"{username} your password is {code}!\n You have {5 - user.attempt} attempts"

                    send_mail(
                        subject='Here is your password',
                        message=mail_content,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[receiver_address]
                    )
                    if user.code:
                        user.code = ''
                    user.attempt += 1
                    user.code = code
                    user.email = email
                    user.save()

                    return Response({
                        'success': f"The message was sent successfully! You have {6 - user.attempt} attempts!"
                    })

                return Response({
                    'error': "Check your gmail login please!"
                })
            else:
                return Response({
                    "error": "You cannot recieve a password!"
                })
        else:
            new_user = User(date_joined=now, username=username, is_active=True, email=email, code=code,
                            role="buyer", attempt=1)
            new_user.save()
            receiver_address = email
            mail_content = f"{username} your password is {code}!\n You have {6 - new_user.attempt} attempts"

            send_mail(
                subject='Here is your password',
                message=mail_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[receiver_address]
            )
            return Response({
                'success': f"The message was sent successfully! You have {6 - new_user.attempt} attempts!"
            })


class LoginCodeView(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data['name']
        password = request.data['password']
        email = request.data['email']
        code = request.data['code']
        user = User.objects.get(username=username, code=code)
        now = datetime.now()

        if username == user.username and email in user.email and code in user.code:
            token = Token.objects.filter(user=user)
            if token:
                token.delete()
            token = Token(user=user)
            token.save()
            if user.code:
                user.code = ''
                user.save()
            if user.last_login:
                user.last_login = ''
                user.save()
            user.last_login = now
            user.role = "buyer"
            user.set_password(password)
            user.save()
            return Response({
                'token': token.key,
                'user_id': user.id
            })
        else:
            return Response({
                'error': "Code or Email not correct"
            })
