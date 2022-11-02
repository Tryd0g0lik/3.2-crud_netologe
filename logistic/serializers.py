from rest_framework import serializers
from logistic.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=('id', 'title', 'description')


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    product = serializers.CharField()
    stock = serializers.CharField()
    price = serializers.IntegerField()
    class Meta:
        model = StockProduct
        fields = ('id', 'stock', 'product', 'price', 'quantity')

class StockSerializer(serializers.ModelSerializer):
    address=serializers.CharField(max_length=30)
    positions = ProductPositionSerializer(many=True, )

    class Meta:
        model = Stock
        fields = ('address', 'positions')

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(**validated_data)
        for data_poss in positions:
            StockProduct.objects.create(stock=stock, **data_poss)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock


    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        for data_poss in positions:
            StockProduct.objects.create(stock=stock, **data_poss)
        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock

