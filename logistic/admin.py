from django.contrib import admin
from logistic.models import *
# Register your models here.

class StockProductInline(admin.TabularInline):
	model = StockProduct
	list_display = ['stock', 'product', 'quantity', 'price', ]
	extra=0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display=['id', 'title', 'description',]
	search_fields=('title',)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
	list_display=['id', 'address',]
	list_filter=['address', ]
	search_fields = ('address', 'products',)

	inlines=[StockProductInline, ]

# class StockProductAdmin(admin.ModelAdmin):
# 	list_display = ['stock', 'product', 'quantity', 'price',]
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Stock, StockAdmin)