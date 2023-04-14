from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from .models import User
from .serializers import CreateUserSerializer, UserSerializer


@extend_schema(tags=["users"])
class RegisterUserView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = AccessToken.for_user(user)
            refresh = RefreshToken.for_user(user)
            response_data = {
                'dni': user.dni,
                'email': user.email,
                'token': str(token),
                'refresh': str(refresh),
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["users"])
class AdminUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
