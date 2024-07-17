from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartItemViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
