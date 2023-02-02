from django.contrib import admin
from . models import Category,Subcategory,Product,Order


# Register your models here.

admin.site.site_header="My Inventory Dashboard"

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','subcategory','quantity')
    list_filter=['subcategory']
    list_editable=['quantity']

class SubcategoryAdmin(admin.ModelAdmin):
    list_display=('category','name')

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Subcategory,SubcategoryAdmin)
