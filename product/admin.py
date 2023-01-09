from django.contrib import admin
from product.models import *

MAX_OBJECTS = 1

# Register your models here.
admin.site.register(ProductImage)


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 3
    extra = 1


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    inlines = [ProductImageInline, ]
    list_display = ['name','created_date']


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['title']




