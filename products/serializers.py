from rest_framework import serializers
from .models import Category, Product, Cart


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
        ]

class ProductSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "name",
            "slug",
            "description",
            "price",
            "stock",
            "image",
            "is_available",
        ]

class CartSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    product_price = serializers.DecimalField(
        source="product.price",
        max_digits=10,
        decimal_places=2,
        read_only=True
    )
    product_image = serializers.ImageField(
    source="product.image",
    read_only=True
)

    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = [
            "id",
            "product",
            "product_name",
            "product_price",
            "product_image",
            "quantity",
            "total_price",
        ]