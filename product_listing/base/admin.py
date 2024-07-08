from django.contrib import admin

from .models import Category,Product,Region,Shop

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Region)
admin.site.register(Shop)