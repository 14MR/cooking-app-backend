from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from recipes.models import Recipe, RecipeStep, RecipeImageBlock, RecipeTextBlock, RecipeTimerBlock


class RecipeImageBlockSerializer(serializers.ModelSerializer):
    image_url = serializers.CharField(source='image.url')

    class Meta:
        model = RecipeImageBlock
        fields = ("type", "image_url")


class RecipeTextBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeTextBlock
        fields = ("type", "text")


class RecipeTimerBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeTimerBlock
        fields = ("type", "time")


serializers_map = {
    RecipeImageBlock: RecipeImageBlockSerializer,
    RecipeTextBlock: RecipeTextBlockSerializer,
    RecipeTimerBlock: RecipeTimerBlockSerializer
}


class RecipeStepSerializer(serializers.ModelSerializer):
    blocks = serializers.SerializerMethodField()

    class Meta:
        model = RecipeStep
        fields = ("blocks", "name", "time")

    @swagger_serializer_method(serializer_or_field=RecipeTimerBlockSerializer)
    def get_blocks(self, obj):
        blocks = map(lambda x: serializers_map[type(x)](x).data, obj.blocks.all())
        return blocks


class RecipeSerializer(serializers.ModelSerializer):
    steps = RecipeStepSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ("id", "name", "total_time", "author", "steps", "description")


class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ("id", "name", "description")
