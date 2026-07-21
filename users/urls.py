from django.urls import path
from .views import (RegisterAPIView, 
    ProfileAPIView, 
    ChangePasswordAPIView,
    LogoutAPIView)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    # Login
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

    # Refresh Token
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("profile/", ProfileAPIView.as_view(), name="profile"),
    path("change-password/", ChangePasswordAPIView.as_view(), name="change_password"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
]