from django.contrib import admin

from users.models import User
from shop.admin import BasketAdminInLine


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInLine,)
