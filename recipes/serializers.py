from rest_framework import serializers

from recipes.models import Recipe, RecipeStep


class RecipeStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ("id", "name", "total_time", "author")


class RecipeSerializer(serializers.ModelSerializer):
    steps = serializers.SerializerMethodField()
    class Meta:
        model = Recipe
        fields = ("id", "name", "total_time", "author", "steps")

    def get_steps(self):
        return []



class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ("id", "name",)
