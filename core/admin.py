from django.contrib import admin

# Register your models here.
from user.models import CustomerUser
from product.models import Product, Category, Variation, Post , Comment
from cart.models import Cart, CartItem
from order.models import Order
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['price']
    search_fields = ['title']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'date']
    list_filter = ['date']
    search_fields = ['title']

class CommentAdmin(admin.ModelAdmin):
    list_filter = ['date']


admin.site.register(Product, ProductAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Variation)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(CustomerUser)