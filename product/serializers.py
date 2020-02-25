from rest_framework import serializers
from .models import Product

class GetAllProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', )