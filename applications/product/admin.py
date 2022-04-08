from django.contrib import admin
from applications.product.models import *

# Register your models here.

admin.site.register(Categore)
# admin.site.register(Product)
admin.site.register(Image)


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInAdmin
    ]