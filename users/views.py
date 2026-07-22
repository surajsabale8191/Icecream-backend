from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer, ProfileSerializer, ChangePasswordSerializer, LogoutSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class RegisterAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "status": True,
                    "message": "User registered successfully."
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)

        return Response(
            {
                "status": True,
                "data": serializer.data
            }
        )

    def put(self, request):
        serializer = ProfileSerializer(
            request.user,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "status": True,
                    "message": "Profile updated successfully.",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):

        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():

            user = request.user

            # Verify old password
            if not user.check_password(
                serializer.validated_data["old_password"]
            ):
                return Response(
                    {
                        "status": False,
                        "message": "Old password is incorrect."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Set new password
            user.set_password(
                serializer.validated_data["new_password"]
            )
            user.save()

            return Response(
                {
                    "status": True,
                    "message": "Password changed successfully."
                }
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = LogoutSerializer(data=request.data)

        if serializer.is_valid():
            try:
                token = RefreshToken(serializer.validated_data["refresh"])
                token.blacklist()

                return Response(
                    {
                        "status": True,
                        "message": "Logged out successfully."
                    }
                )

            except Exception:
                return Response(
                    {
                        "status": False,
                        "message": "Invalid refresh token."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        return Response(serializer.errors)

