from django.contrib import admin

# Register your models here.
from .models import Product, Phone1, Order, OrderUpdate
admin.site.register(Product)
admin.site.register(Phone1)
admin.site.register(Order)
admin.site.register(OrderUpdate)