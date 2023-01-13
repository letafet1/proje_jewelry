from django.contrib import admin
from product.models import *

MAX_OBJECTS = 1

# Register your models here.


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','created_date']


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['title']




