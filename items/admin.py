from django.contrib import admin
from items.models import Item, ItemParam


class ParamInline(admin.TabularInline):
    model = ItemParam


class ItemAdmin(admin.ModelAdmin):
    inlines = [ParamInline]

admin.site.register(Item, ItemAdmin)
