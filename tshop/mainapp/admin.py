from django.contrib import admin
from.models import Product
# Register your models here.

# Every model registred here will be accessible in the django admin panel
admin.site.register(Product)