from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer, RecipeListSerializer, CreateRecipeStepSerializer
from recipes.serializers.write import CreateRecipeSerializer


class RecipesViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing recipes.
    """
    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return RecipeListSerializer
        return RecipeSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateRecipeSerializer(data={'author_id': request.user.id, **request.data})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def step(self, request, pk=None, *args, **kwargs):
        recipe = Recipe.objects.get(pk=pk)

        serializer = CreateRecipeStepSerializer(data={'recipe_id': recipe.id, **request.data})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)
