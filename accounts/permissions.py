from rest_framework import permissions

class CustomPermission(permissions.BasePermission):
    message = "Sizda bu amalni bajarish uchun yetarli huquq yo'q."

class IsAdmin(permissions.BasePermission):
    """Admin roliga ruxsat beruvchi permission"""
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'Admin'
        )

class IsCustomer(permissions.BasePermission):
    """Customer roliga ruxsat beruvchi permission"""
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'Customer'
        )

class IsManager(permissions.BasePermission):
    """Manager roliga ruxsat beruvchi permission"""
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'Manager'
        )
