from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel


class CustomUserAdmin(UserAdmin):
    # Admin panelda ko‘rinadigan ustunlar
    list_display = ('username', 'email', 'role', 'phone_number', 'date_of_birth', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('username',)

    # Formda ko‘rinadigan maydonlar
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'role', 'address', 'phone_number', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'address', 'phone_number', 'date_of_birth', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )


admin.site.register(UserModel, CustomUserAdmin)