from django.contrib import admin

# Register your models here.
from .models import Category, Item, Unit, UnitConversion, Customer, Sale, Row

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Unit)
admin.site.register(UnitConversion)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(Row)