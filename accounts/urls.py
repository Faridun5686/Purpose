from django.urls import path
from .views import (
  UserRegisterView,
  AdminOnlyView,
  CustomerOnlyView,
  ManagerOnlyView,
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('admin_authors/', AdminOnlyView.as_view(), name='admin-authors'),
    path('custom/', CustomerOnlyView.as_view(), name='custom'),
    path('manager/profile/', ManagerOnlyView.as_view(), name='manager'),
]
