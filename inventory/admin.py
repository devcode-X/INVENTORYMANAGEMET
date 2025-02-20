from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'updated_at')
    search_fields = ('name',)

# from django.contrib import admin
# from .models import Product

# admin.site.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'quantity', 'updated_at')
#     search_fields = ('name',)
