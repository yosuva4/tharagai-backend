from django.contrib import admin

from api.model.product_model import Product,ProductType,ProductVariation,SkinType,Benefits,HowtoUse,Ingredients,Cart
from api.model.user_model import UserAddress



admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductVariation)
admin.site.register(SkinType)
admin.site.register(Benefits)
admin.site.register(HowtoUse)
admin.site.register(Ingredients)

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_product_name', 'item_count']
    
    def get_product_name(self, obj):
        return obj.product.product.name
    
    get_product_name.short_description = 'Product Name'

admin.site.register(Cart, CartAdmin)


admin.site.register(UserAddress)