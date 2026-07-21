from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

class CategoryAPIView(APIView):

    def get(self, request):

        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)

        return Response(
            {
                "status": True,
                "data": serializer.data
            }
        )


class ProductAPIView(APIView):

    def get(self, request):

        products = Product.objects.filter(is_available=True)

        search = request.GET.get("search")

        if search:
            products = products.filter(name__icontains=search)
        category = request.GET.get("category")

        if category:
            products = products.filter(
        category__slug=category
        )
        serializer = ProductSerializer(products, many=True)

        return Response(
            {
                "status": True,
                "data": serializer.data
            }
        )




class ProductDetailAPIView(APIView):

    def get(self, request, pk):

        product = get_object_or_404(
            Product,
            pk=pk,
            is_available=True
        )

        serializer = ProductSerializer(product)

        return Response({
            "status": True,
            "data": serializer.data
        })