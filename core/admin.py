from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'category')
    list_filter = ('category',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'product', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_name', 'customer_email', 'product__name')
    readonly_fields = ('created_at',)
