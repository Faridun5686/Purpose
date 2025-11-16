from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """Foydalanuvchi Admin bo'lsa ruxsat beradi"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Admin'

class IsManager(permissions.BasePermission):
    """Foydalanuvchi Manager bo'lsa ruxsat beradi"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Manager'

class IsCustomer(permissions.BasePermission):
    """Foydalanuvchi Customer bo'lsa ruxsat beradi"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Customer'
