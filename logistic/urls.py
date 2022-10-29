from rest_framework.routers import DefaultRouter
from django.urls import path

import logistic.views
from logistic.views import ProductViewSet, StockViewSet



router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

# urlpatterns = router.urls

urlpatterns = [
	# path('', logistic.views.ProductViewSet)
] + router.urls
