from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer,LoginSerializer
from rest_framework import status

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"account created sucussfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = LoginSerializer(data = request.data, context = {"request": request})
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            return Response(
                {
                    "message": "Login successful",
                    "username": user.username,
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "You are authenticated",
            "username": request.user.username,
            "email": request.user.email,
        })
