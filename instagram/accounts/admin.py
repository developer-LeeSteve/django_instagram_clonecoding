from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser

class CustomUserAdmin(UserAdmin):
	list_display = ('email', 'username', 'name', 'date_joined', 'is_staff', 'is_active')
	search_fields = ()
	fieldsets=(
		(None, {'fields': ('email', 'password')}),
		('Personal Info', {'fields': ('username', 'name', 'date_of_birth', 'profile_pic')}),
		('Permissions', {'fields': ('is_admin',)}),
	)
	add_fieldsets=(
		(None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
	)

admin.site.register(CustomUser, CustomUserAdmin)