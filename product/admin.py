from django.contrib import admin
from .models import Color,Category,creator,Type,Product
from product.models import Order, OrderItem

# Register your models here.
class ColorAdmin(admin.ModelAdmin):
    list_display = ('code','name')
    list_filter = ('code','name')
    search_fields = ('code','name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code','name')
    list_filter = ('code','name')
    search_fields = ('code','name')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('code','name')
    list_filter = ('code','name')
    search_fields = ('code','name')

class CreatorsAdmin(admin.ModelAdmin):
    list_display = ('code','name')
    list_filter = ('code','name')
    search_fields = ('code','name')

class ProductAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('barcode','name','typ','category','color','size','quantity','priceIn','priceOut','date_published','active')
    list_filter =('barcode','name','typ','category','color','size','quantity','priceIn','priceOut','date_published','active')
    # readonly_fields =('barcode','name','typ','category','color','size','quantity','priceIn','priceOut',)
    search_fields =('barcode','name','typ','category','color','size','quantity','priceIn','priceOut','date_published','active')
    

class OrderItemAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('user','ordered','item','quantity',)
    list_filter =('user','ordered','item','quantity',)
    # readonly_fields =('barcode','name','typ','category','color','size','quantity','priceIn','priceOut',)
    search_fields =('user','ordered','item','quantity',)
    



class OrderAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('user','emp','get_products','order_date','ordered',)
    list_filter =('user','emp','order_date','ordered',)
    # readonly_fields =('barcode','name','typ','category','color','size','quantity','priceIn','priceOut',)
    search_fields =('user','emp','get_products','order_date','ordered',)
    



admin.site.register(Color,ColorAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(creator,CreatorsAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(Product,ProductAdmin)

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)

