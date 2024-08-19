from django.contrib import admin
from .models import Product

# command to administrate the Product class at the admin panel
admin.site.register(Product)