from django.contrib import admin
from . models import Category,Product,Order


# Register your models here.

admin.site.site_header="My Inventory Dashboard"

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity')
    list_filter=['category']
    list_editable=['quantity']

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(Category)
