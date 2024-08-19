from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


# command to administrate the Product class at the admin panel
admin.site.register(Product, ProductAdmin)
