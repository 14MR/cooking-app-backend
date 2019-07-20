from django.http import JsonResponse
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer, RecipeListSerializer
from users.models import User
from users.serializers import UserSerializer


class RecipesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing recipes.
    """
    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return RecipeListSerializer
        return RecipeSerializer
