from django.contrib import admin

from stocks.models import Category, Price, Stock, Warehouse


class StockAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)
admin.site.register(Price)
admin.site.register(Stock, StockAdmin)
admin.site.register(Warehouse)
