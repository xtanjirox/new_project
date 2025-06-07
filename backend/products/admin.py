from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'description')
    list_filter = ('company',)
    search_fields = ('name', 'description')
    list_per_page = 20

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'category', 'sku', 'base_price', 'ttc_price', 'stock_quantity', 'is_active')
    list_filter = ('company', 'category', 'is_active')
    search_fields = ('name', 'description', 'sku', 'barcode')
    list_editable = ('base_price', 'ttc_price', 'stock_quantity', 'is_active')
    list_per_page = 20
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'company', 'description', 'category', 'image')
        }),
        ('Inventory Details', {
            'fields': ('sku', 'barcode', 'base_price', 'ttc_price', 'cost_price', 'stock_quantity', 'min_stock_level', 'is_active')
        }),
    )