from rest_framework import serializers

from recipes.enums import RecipeBlockType
from recipes.models import Recipe, RecipeStep, RecipeTextBlock, RecipeImageBlock


class CreateRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('name', 'author_id', 'description')


class CreateRecipeStepSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        recipe = validated_data['recipe_id']
        blocks = validated_data['blocks']
        block = None
        step = RecipeStep.objects.create(name=validated_data['name'], time=validated_data['time'], recipe=recipe)

        for block in blocks:
            if block['type'] == 'text':
                block = RecipeTextBlock.objects.create(
                    step=step,
                    text=block['text']
                )
            elif block['type'] == 'image':
                images_data = self.context.get('view').request.FILES.values()
                block = RecipeImageBlock.objects.create(
                    step=step,
                    image=images_data[0]
                )
        return block

    name = serializers.CharField(max_length=255)
    # text = serializers.CharField()
    recipe_id = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())
    # type = serializers.CharField()
    time = serializers.IntegerField(min_value=0, max_value=24 * 60 * 60)
    blocks = serializers.ListSerializer(child=serializers.JSONField())
