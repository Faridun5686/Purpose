from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Post yoki Comment muallifiga tahrirlash huquqi beradi.
    Boshqalar faqat o'qishi mumkin.
    """
    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS so'rovlar har doim ruxsatli
        if request.method in permissions.SAFE_METHODS:
            return True
        # Muallif faqat o'zi yaratgan post/commentni tahrirlashi mumkin
        return obj.author == request.user
