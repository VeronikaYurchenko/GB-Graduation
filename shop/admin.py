from django.contrib import admin

from shop.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    readonly_fields = ('short_description',)
    ordering = ('name',)
    search_fields = ('name',)


class BasketAdminInLine(admin.TabularInline):
    model = Basket
    fields = ('products', 'quantity', 'created_timestamp')
    readonly_fields = ('product', 'created_timestamp')
    extra = 0