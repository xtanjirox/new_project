from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    fields = ('product', 'quantity', 'unit_price', 'total_price')
    readonly_fields = ('total_price',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'company', 'client', 'status', 'created_at', 'total')
    list_filter = ('status', 'company', 'created_at')
    search_fields = ('order_number', 'client__name', 'shipping_address')
    readonly_fields = ('order_number', 'total', 'created_at', 'updated_at')
    inlines = [OrderItemInline]
    list_per_page = 20
    fieldsets = (
        ('Basic Information', {
            'fields': ('company', 'client', 'created_by', 'order_number', 'status')
        }),
        ('Shipping Information', {
            'fields': ('shipping_address', 'shipping_city', 'shipping_state', 'shipping_country', 'shipping_zip_code')
        }),
        ('Financial Details', {
            'fields': ('subtotal', 'tax', 'shipping_cost', 'discount', 'total')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price', 'total_price')
    list_filter = ('order__status',)
    search_fields = ('order__order_number', 'product__name')
    readonly_fields = ('total_price',)
    list_per_page = 20