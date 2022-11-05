from rest_framework import serializers
from logistic.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=('__all__')


class ProductPositionSerializer(serializers.ModelSerializer):
    product = serializers.CharField()
    class Meta:
        model = StockProduct
        fields = ('__all__')

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True, write_only=True )


    class Meta:
        model = Stock
        exclude=['products']

