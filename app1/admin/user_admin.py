from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from app1.models.custome_user import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model=User
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

     #aita code toko chara django USER e shudu user namr khujbe,,kinto ai kahne to user name nai,tai user name bad dite hobe
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff')}),
        ('Permissions', {'fields': ('is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active')}
        ),
    )

    