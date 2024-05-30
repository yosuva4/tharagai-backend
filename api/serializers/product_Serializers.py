from rest_framework import serializers

from api.model.product_model import Product,ProductType,ProductVariation,SkinType,HowtoUse,Benefits,Ingredients,Cart


class SkinTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinType
        fields = ['id','skinType']
        
class HowtoUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowtoUse
        fields = ['id','how_to_use']
        
class BenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits
        fields = ['id','benefit']
        
class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['ingredients']

class ProductVariationSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductVariation
        fields = ["id",'weight','price','oldPrice']
    
class ProductSerializers(serializers.ModelSerializer):
    product_type_name = serializers.ReadOnlyField(source='product_type.name')
    variations = serializers.SerializerMethodField(read_only=True)
    skintype = serializers.SerializerMethodField(read_only=True)
    howtouse = serializers.SerializerMethodField(read_only=True)
    benefit = serializers.SerializerMethodField(read_only=True)
    ingredients = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name','image','description', 'product_type_name','variations','skintype','howtouse','benefit','ingredients']
        
    def get_variations(self,obj):
        variations = obj.productvariation_set.all()
        serializer = ProductVariationSerializers(variations,many=True)
        return serializer.data
    
    def get_skintype(self,obj):
        return SkinTypeSerializer(obj.skintype_set.all(),many=True).data
    
    def get_howtouse(self,obj):
        return HowtoUseSerializer(obj.howtouse_set.all(),many=True).data
    
    def get_benefit(self,obj):
        return BenefitsSerializer(obj.benefits_set.all(),many=True).data
    
    def get_ingredients(self,obj):
        return IngredientsSerializer(obj.ingredients_set.all(),many=True).data
    
    def create(self, validated_data):
        print("validated_data : ",validated_data)
        return super().create(validated_data)
       
class ProductTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"
    
class CartSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    image = serializers.ImageField(source='product.product.image', read_only=True)
    price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    _id = serializers.IntegerField(source='product.id', read_only=True)

    def get_product_name(self, obj):
        return obj.product.product.name

    class Meta:
        model = Cart
        fields = ["id",'user', 'product_name', 'item_count', 'total_cart', 'image', 'price','_id']

