from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from .serializers import UserRegisterSerializer
from .models import UserModel
from .permissions import IsAdmin, IsCustomer, IsManager


# Foydalanuvchi ro'yxatdan o'tishi
class UserRegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Faqat Adminlar ko'ra oladigan ro'yxat
class AdminOnlyView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


# Faqat Customer rolidagi foydalanuvchi profili
class CustomerOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsCustomer]
    serializer_class = UserRegisterSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Faqat Manager profili
class ManagerOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsManager]
    serializer_class = UserRegisterSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
