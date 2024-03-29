# Generated by Django 3.2 on 2022-11-21 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping', '0013_alter_category_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['id'], 'verbose_name': 'Brand', 'verbose_name_plural': 'Brands'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['id'], 'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['id'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-id'], 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['id'], 'verbose_name': 'SubCategory', 'verbose_name_plural': 'SubCategories'},
        ),
        migrations.AlterModelOptions(
            name='wishlist',
            options={'ordering': ['-id'], 'verbose_name': 'WishList', 'verbose_name_plural': 'WishLists'},
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name of Company'),
        ),
        migrations.AlterField(
            model_name='category',
            name='city',
            field=models.ManyToManyField(to='shopping.City', verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_image/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=80, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.PositiveIntegerField(default=1, verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='product',
            name='article',
            field=models.IntegerField(null=True, unique=True, verbose_name='Article'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Date public'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_creater', to=settings.AUTH_USER_MODEL, verbose_name='Creater'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cur',
            field=models.CharField(choices=[('SOM', 'Сом'), ('USD', 'Доллар'), ('EURO', 'Евро'), ('RUB', 'Рубль')], default='SOM', max_length=4, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_image/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, to='shopping.subcategory', verbose_name='SubCategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateField(auto_now=True, verbose_name='Date update'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(upload_to='subcategory_image/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Sub Category'),
        ),
    ]
