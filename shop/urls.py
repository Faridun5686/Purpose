from django.urls import path
from .views import (
    ProductListCreateView,
    ProductDetailView,
    OrderListCreateView,
    OrderDetailView,
    CartListCreateView,
    CartDetailView,
)

urlpatterns = [
    # Product
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Order
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

    # Cart
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
]
