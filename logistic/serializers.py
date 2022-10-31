from rest_framework import serializers
from logistic.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    # pass
    class Meta:
        model = StockProduct
        fields = ['id', 'stock', 'product', 'price',]

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions',]
    # настройте сериализатор для склада

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        print(f"positions: {positions}")
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        print(f"stock: {stock}")
        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock

# не могу написать самописные методы обновления и удаления в сериализаторе ModelSerializer

# Так как продуктов и складов может быть много, то необходимо реализовать пагинацию для вывода списков.