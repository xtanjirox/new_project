from django.contrib import admin
from .models import Invoice, InvoiceItem, Payment

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 0
    fields = ('description', 'quantity', 'unit_price', 'total_price')
    readonly_fields = ('total_price',)

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0
    fields = ('amount', 'payment_date', 'payment_method', 'reference_number')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'company', 'client', 'status', 'issue_date', 'due_date', 'total', 'is_overdue')
    list_filter = ('status', 'company', 'issue_date', 'due_date')
    search_fields = ('invoice_number', 'client__name', 'notes')
    inlines = [InvoiceItemInline, PaymentInline]
    readonly_fields = ('total', 'subtotal', 'balance_due', 'is_overdue', 'created_at', 'updated_at')
    list_per_page = 20
    fieldsets = (
        ('Basic Information', {
            'fields': ('company', 'client', 'order', 'invoice_number', 'status')
        }),
        ('Dates', {
            'fields': ('issue_date', 'due_date')
        }),
        ('Financial Details', {
            'fields': ('subtotal', 'tax_amount', 'discount_amount', 'total', 'balance_due')
        }),
        ('Additional Information', {
            'fields': ('notes', 'is_overdue')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'description', 'quantity', 'unit_price', 'total_price')
    search_fields = ('invoice__invoice_number', 'description')
    readonly_fields = ('total_price',)
    list_per_page = 20

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'amount', 'payment_date', 'payment_method', 'reference_number')
    list_filter = ('payment_method', 'payment_date')
    search_fields = ('invoice__invoice_number', 'reference_number')
    list_per_page = 20