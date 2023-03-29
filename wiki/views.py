from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Category, Tema, Wiki
from .permissions import IsOwnerOrAdmin
from .serializers import CategorySerializer, TemaSerializer, WikiSerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class TemaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer
    permission_classes = [IsOwnerOrAdmin]


class TemaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer
    permission_classes = [IsOwnerOrAdmin]


class WikiListCreateAPIView(generics.ListCreateAPIView):
    queryset = Wiki.objects.all()
    serializer_class = WikiSerializer
    permission_classes = [IsAuthenticated]


class WikiRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wiki.objects.all()
    serializer_class = WikiSerializer
    permission_classes = [IsOwnerOrAdmin]
