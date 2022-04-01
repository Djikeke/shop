from django.contrib import admin
from applications.product.models import Categore, Product

# Register your models here.

admin.site.register(Categore)
admin.site.register(Product)