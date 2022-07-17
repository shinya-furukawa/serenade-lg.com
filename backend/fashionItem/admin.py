from django.contrib import admin
from fashionItem.models import Item,ItemDetail,Category,SubCategory

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'itemname',
        'price',
        'id',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'id'
    )

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sub_category_name',
        'id'
    )

class DetailAdmin(admin.ModelAdmin):
    list_display = (
        'item',
        'color',
        'itemcount'
    )

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemDetail,DetailAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)

