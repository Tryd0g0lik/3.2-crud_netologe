from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from logistic.models import *

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer, ProductPositionSerializer



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends =[SearchFilter, DjangoFilterBackend]
    search_fields=['id', 'title', 'description']
    filterset_fields=['id',]

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    # при необходимости добавьте параметры фильтрации
    filter_backends=[SearchFilter, DjangoFilterBackend]
    search_fields=['address']
    filterset_fields=['id',]

class StockProductViewSet(ModelViewSet):
    queryset=StockProduct.objects.all()
    serializer_class=ProductPositionSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields=['product', 'quantity', 'price', 'stock']


