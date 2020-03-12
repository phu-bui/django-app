from django.db import models
from django.db.models import Q
from django.conf import settings
class Category(models.Model):
    title = models.CharField(max_length=100 , default='')
    slug = models.CharField(max_length=45, default='')
    description = models.TextField( default='')
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Product (models.Model):
    title = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    description = models.TextField(default='')
    brand = models.CharField(max_length=100, default='')
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Variation(models.Model):
    title = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    action = models.BooleanField(default=True)
    inventory = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100, default='')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.post.title


class ProductManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(description__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs
