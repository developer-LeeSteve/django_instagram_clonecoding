from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, FollowingRelationships, BlockedRelationships

class CustomUserAdmin(UserAdmin):
	list_display = ('email', 'username', 'name', 'date_joined', 'is_staff', 'is_active')
	search_fields = ()
	fieldsets=(
		(None, {'fields': ('email', 'password')}),
		('Personal Info', {'fields': ('username', 'name', 'date_of_birth', 'profile_pic',)}),
		('Permissions', {'fields': ('is_admin',)}),
	)
	add_fieldsets=(
		(None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'username', 'password1', 'password2', 'date_of_birth', 'profile_pic'),
        }),
	)


admin.site.register(User, CustomUserAdmin)
admin.site.register(FollowingRelationships)
admin.site.register(BlockedRelationships)

admin.site.site_header = 'Django Admin Page'
admin.site.index_title = 'Django Admin'