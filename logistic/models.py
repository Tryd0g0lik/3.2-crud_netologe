from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60, unique=True,
                             verbose_name='Название',
                             default='None')
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Описание')
    def __str__(self):

        return "%s" % (self.title,)

    class Meta:
        verbose_name='Товар'
        verbose_name_plural = 'Продукты'
        ordering=['title',]

class Stock(models.Model):
    address = models.CharField(max_length=200)
    products = models.ManyToManyField(
        Product,
        through='StockProduct',

    )

    def __str__(self):
        return """%s""" % (self.address,)

    class Meta:
        verbose_name = 'Адрес склада'
        verbose_name_plural='Адреса'
        ordering=['address',]

class StockProduct(models.Model):
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        verbose_name='Склады',
        related_name='positions',

    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='positions',


    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
