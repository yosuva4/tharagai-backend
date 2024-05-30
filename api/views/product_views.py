from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.exceptions import NotFound

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from api.serializers.product_Serializers import ProductSerializers,CartSerializer,ProductTypeSerializers
from api.model.product_model import *


class BestSeller(APIView):
    def get(self,request):
        product = Product.objects.filter(bestSeller=True).order_by('id')
        serializer = ProductSerializers(product, many=True)
        return Response(status=200, data=serializer.data) 

class Products(ListAPIView):
    model = Product
    serializer_class = ProductSerializers
    queryset = Product.objects.all().order_by("id")
 
class ProductTypeView(ListAPIView):
    model = ProductType
    serializer_class = ProductTypeSerializers
    queryset = ProductType.objects.filter().order_by("id")   

class FilterProduct(APIView):
    def get(self, request, pk):
        try:
            product_type = get_object_or_404(ProductType, name=pk)
            product = Product.objects.filter(product_type=product_type).order_by('id')
            serializer = ProductSerializers(product, many=True)
            return Response(status=200, data=serializer.data)   
        except NotFound:
            return Response(status=404, data={"error": "ProductType not found"})
        except Exception as e:
            return Response(status=500, data={"error": str(e)})
         
class ProductGet(APIView):
    def get(self,request,pk):
        return Response(ProductSerializers(Product.objects.get(id=pk)).data)
    
class ProductAdd(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    def post(self,request):
        print("Hello Post ")
        try:
            data = request.data
            # # Ensure required fields exist in data
            required_fields = ['name', 'productTitle', 'product_type_name', 'description', 'image', 'variations', 'howtouse', 'ingredients','skintype']
            for field in required_fields:
                if field not in data:
                    return Response(status=400, data={"error": f"Missing required field: {field}"})

            image = request.FILES.get('image', None)

            product_type, created = ProductType.objects.get_or_create(name=data['product_type_name'])
                
            product = Product.objects.create(
                name=data['name'],
                product_type=product_type,
                productTitle=data['productTitle'],
                description=data['description'],
                # image=data["image"]  # Assuming image URL is provided directly
            )
            variations_data = data['variations']
            
            for variation_data in variations_data:
                ProductVariation.objects.create(
                    product=product,
                    weight=variation_data['weight'],
                    price=variation_data['price']
                )
            # # Create other related instances
            for skintype_data in data['skintype']:
                SkinType.objects.create(
                    product=product,
                    skinType=skintype_data['skinType']
                )
            
            for howtouse_data in data['howtouse']:
                HowtoUse.objects.create(
                    product=product,
                    how_to_use=howtouse_data['howtoUse']
                )
            
            for benefit_data in data['benefit']:
                Benefits.objects.create(
                    product=product,
                    benefit=benefit_data['benefit']
                )
            
            for ingredient_data in data['ingredients']:
                Ingredients.objects.create(
                    product=product,
                    ingredients=ingredient_data['keyIngredients']
                )
            return Response(status=200,data={"message":"All Products Saved!"})
        except Exception as e:
            print("The Error is : ",e)
            
            return Response(status=400,data={"error":"did not saved"})
      
class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        username = request.user.username
        user = User.objects.get(username=username)
        serializer = CartSerializer(Cart.objects.filter(user = user),many=True)
        return Response(status=200,data=serializer.data)
    
    def post(self, request):
        try:
            user = User.objects.get(username=request.user.username)
            data = request.data
            product_variation = ProductVariation.objects.get(pk=data['id'])
            
            try:
                cart_item = Cart.objects.get(user=user, product=product_variation)
                cart_item.item_count = int(data['qty'])
                cart_item.save()
            
            except ObjectDoesNotExist:
                cart_item = Cart(user=user, product=product_variation, item_count=data['qty'])
                cart_item.save()
            
            serializer = CartSerializer(Cart.objects.filter(user = user),many=True)
            return Response(status=200,data=serializer.data)
        
        except Exception as e:
            return Response(status=401, data={"message": "Failed to save product to cart"})
        
    def delete(self,request,id):
        try:            
            username = request.user.username
            try:
                Cart.objects.filter(id=id).delete()
            except Exception as e:
                return Response(status=401, data={"message": "Failed to Delete product to cart"})
                
            user = User.objects.get(username=username)
            serializer = CartSerializer(Cart.objects.filter(user = user),many=True)
            return Response(status=200,data=serializer.data)
        
        except Exception as e:
            return Response(status=401, data={"message": "Failed to Delete product to cart"})

