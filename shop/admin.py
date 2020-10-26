from django.contrib import admin
from .models import Product,Category
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','category','created']
    list_filter=('created','update')
    pre_populated_fields={'slug':('name',)}
    # list_editable=['name','price']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
