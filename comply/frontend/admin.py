from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from . import models

fields = list(UserAdmin.fieldsets)
fields[0] = (None, {'fields': ('username','password','phone_number','company','role')})
UserAdmin.fieldsets = tuple(fields)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'is_staff', 'last_login') # Added last_login

admin.site.register(User, CustomUserAdmin)
admin.site.register(models.Company)
admin.site.register(models.Location)
admin.site.register(models.Product)
admin.site.register(models.ProductFileType)
admin.site.register(models.ProductFile)
