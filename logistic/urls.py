from rest_framework.routers import DefaultRouter
from django.urls import path

import logistic.views
from logistic.views import ProductViewSet, StockViewSet, StockProductViewSet



router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)
router.register('position', StockProductViewSet)


urlpatterns = [

] + router.urls

