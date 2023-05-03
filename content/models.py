from user.models import User
from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Blog(models.Model):
    name = models.CharField( max_length=150, verbose_name='Blog name')
    context = models.TextField(verbose_name='Context')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(verbose_name='Image', upload_to='blog/', default='product_image/Груша.jpg')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'blogs'
        ordering = ['id']

    def __str__(self):
        return self.name
