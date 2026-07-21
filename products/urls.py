from django.urls import path

from .views import (
    CategoryAPIView,
    ProductAPIView,
    ProductDetailAPIView,
)

urlpatterns = [
    path("categories/", CategoryAPIView.as_view(), name="categories"),
    path("products/", ProductAPIView.as_view(), name="products"),
    path(
    "products/<int:pk>/",
    ProductDetailAPIView.as_view(),
    name="product_detail",
),

]