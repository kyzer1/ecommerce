from .models import Category, Product
from django.contrib import admin


admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = ('category',)
