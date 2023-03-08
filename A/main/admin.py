from django.contrib import admin
from .models import Category, SubCategory, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'price')

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product, ProductAdmin)
