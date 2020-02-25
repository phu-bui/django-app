from django.contrib import admin

# Register your models here.
from user.models import CustomerUser
from product.models import Product, Category, Variation
from cart.models import Cart, CartItem
from order.models import Order
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['price']
    search_fields = ['title']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Variation)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(CustomerUser)