from rest_framework.serializers import ModelSerializer

from .models import Category, Tema, Wiki


class WikiSerializer(ModelSerializer):
    class Meta:
        model = Wiki
        # TODO Por defecto el usuario que crea el wiki es el usuario logueado
        exclude = ['created_at', 'updated_at']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TemaSerializer(ModelSerializer):
    class Meta:
        model = Tema
        fields = '__all__'
