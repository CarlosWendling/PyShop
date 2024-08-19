from django.contrib import admin
from .models import Product, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


# command to administrate the model at the admin panel
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)