from django.db import models

from recipes.enums import RecipeBlockType
from django.db.models import Sum

from users.models import User
from django.utils.translation import gettext as _
from polymorphic.models import PolymorphicModel


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, default=None, blank=True)

    def total_time(self):
        return RecipeStep.objects.filter(recipe_id=self.id).aggregate(Sum('time'))['time__sum']


class RecipeStep(models.Model):
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')
    time = models.IntegerField(default=None, null=True)
    order = models.PositiveSmallIntegerField(default=0)


class RecipeBlock(PolymorphicModel):
    type = models.CharField(max_length=100, choices=RecipeBlockType)
    step = models.ForeignKey(RecipeStep, on_delete=models.CASCADE, related_name='blocks')


class RecipeTextBlock(RecipeBlock):
    text = models.TextField(max_length=10000)


class RecipeImageBlock(RecipeBlock):
    image = models.ImageField()


class RecipeTimerBlock(RecipeBlock):
    time = models.PositiveIntegerField(_("Timer value in seconds"))
