from django.db import models
from user.models import CustomerUser
from cart.models import Cart
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=50, default='')
    order_description = models.CharField(max_length=45, default='')
    order_total = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
