from django.contrib import admin
from FashionGAN.models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_filter=['price']
    list_display=['name','display']
admin.site.register(Product)