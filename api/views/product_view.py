from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializer import ProductSerializer
from ..models import Product



@api_view(['GET'])
def getProducts(request):
    serializer = ProductSerializer(Product.objects.all(),many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,pk):
    serializer = ProductSerializer(Product.objects.filter(_id=pk),many=True)
    return Response(serializer.data)