from django.urls import path

from .views import (
    CategoryAPIView,
    ProductAPIView,
    ProductDetailAPIView,
    AddToCartAPIView,
    CartAPIView,
    IncreaseQuantityAPIView,
    DecreaseQuantityAPIView,
    RemoveCartItemAPIView,
    CheckoutAPIView,
    OrderListAPIView,
    OrderDetailAPIView,



)

urlpatterns = [
    path("categories/", CategoryAPIView.as_view(), name="categories"),
    path("products/", ProductAPIView.as_view(), name="products"),
    path(
    "products/<int:pk>/",
    ProductDetailAPIView.as_view(),
    name="product_detail",),

    path(
    "cart/",
    AddToCartAPIView.as_view(),
    name="add_to_cart",),

    path(
    "cart/view/",
    CartAPIView.as_view(),
    name="view_cart",),

    path(
    "cart/increase/<int:cart_id>/",
    IncreaseQuantityAPIView.as_view(),
    name="increase_quantity",),

    path(
    "cart/decrease/<int:cart_id>/",
    DecreaseQuantityAPIView.as_view(),
    name="decrease_quantity",),

    path(
    "cart/remove/<int:cart_id>/",
    RemoveCartItemAPIView.as_view(),
    name="remove_cart_item",),

    path(
    "orders/checkout/",
    CheckoutAPIView.as_view(),
    name="checkout",),  

    path(
    "orders/",
    OrderListAPIView.as_view(),
    name="order_list"),

    path(
    "orders/<int:order_id>/",
    OrderDetailAPIView.as_view(),
    name="order_detail",),

]