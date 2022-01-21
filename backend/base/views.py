from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .products import products
from .serializers import ProductSerializer

# Create your views here.
@api_view(['Get'])
def getRoutes(request):
  return Response('Hello')

@api_view(['Get'])
def getProducts(request):
  products = Product.objects.all()
  seralizer = ProductSerializer(products, many=True)
  return Response(seralizer.data)



@api_view(['Get'])
def getProduct(request, pk):
  product = Product.objects.get(_id=pk)
  serializer = ProductSerializer(product, many=False)
  

  return Response(serializer.data)


  