from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name', 'first_name','last_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff','password')
    ordering = ('-user_name',)
    list_display = ('email', 'user_name', 'first_name','last_name','password',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name','last_name','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name','last_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
# Register your models here.
