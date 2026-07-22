from django.urls import path

from .views import (
    CategoryAPIView,
    ProductAPIView,
    ProductDetailAPIView,
    AddToCartAPIView,
    CartAPIView,

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

]