from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Category, Product, Cart
from .serializers import CategorySerializer, ProductSerializer, CartSerializer
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

class AddToCartAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        product_id = request.data.get("product")

        try:
            product = Product.objects.get(
                id=product_id,
                is_available=True
            )
        except Product.DoesNotExist:

            return Response(
                {
                    "status": False,
                    "message": "Product not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product=product
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        serializer = CartSerializer(cart_item)

        return Response(
            {
                "status": True,
                "message": "Product added to cart.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

class CartAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        cart_items = Cart.objects.filter(user=request.user)

        serializer = CartSerializer(cart_items, many=True)

        return Response(
            {
                "status": True,
                "data": serializer.data
            }
        )

class IncreaseQuantityAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, cart_id):

        try:
            cart_item = Cart.objects.get(
                id=cart_id,
                user=request.user
            )
        except Cart.DoesNotExist:

            return Response(
                {
                    "status": False,
                    "message": "Cart item not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        cart_item.quantity += 1
        cart_item.save()

        serializer = CartSerializer(cart_item)

        return Response(
            {
                "status": True,
                "message": "Quantity increased.",
                "data": serializer.data
            }
        )

class DecreaseQuantityAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, cart_id):

        try:
            cart_item = Cart.objects.get(
                id=cart_id,
                user=request.user
            )
        except Cart.DoesNotExist:

            return Response(
                {
                    "status": False,
                    "message": "Cart item not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

            return Response(
                {
                    "status": True,
                    "message": "Item removed from cart."
                }
            )

        serializer = CartSerializer(cart_item)

        return Response(
            {
                "status": True,
                "message": "Quantity decreased.",
                "data": serializer.data
            }
        )

class RemoveCartItemAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, cart_id):

        try:
            cart_item = Cart.objects.get(
                id=cart_id,
                user=request.user
            )
        except Cart.DoesNotExist:
            return Response(
                {
                    "status": False,
                    "message": "Cart item not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        cart_item.delete()

        return Response(
            {
                "status": True,
                "message": "Item removed successfully."
            }
        )