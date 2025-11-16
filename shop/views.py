from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product, Order, Cart
from .serializers import ProductSerializer, OrderSerializer, CartSerializer
from .permissions import IsAdmin, IsManager, IsCustomer

# Product CRUD
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsManager)]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsManager)]

# Order CRUD
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'Customer':
            return Order.objects.filter(user=user)
        return Order.objects.all()

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

# Cart CRUD
class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated & IsCustomer]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated & IsCustomer]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
