from django.contrib.admin import AdminSite
from rest_framework.authtoken.models import Token

SITE_NAME = "Cooking admin"


class GoodsAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = SITE_NAME
    # Text to put in each page's <h1> (and above login form).
    site_header = SITE_NAME
    # Text to put at the top of the admin index page.
    index_title = SITE_NAME


admin_site = GoodsAdminSite()

from django.contrib import admin

from recipes.models import Recipe, RecipeBlock, RecipeStep, RecipeImageBlock, RecipeTextBlock, RecipeTimerBlock


class RecipeStepInline(admin.TabularInline):
    model = RecipeStep
    show_change_link = True


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeStepInline]


admin_site.register(Recipe, RecipeAdmin)
admin_site.register(RecipeBlock)
admin_site.register(RecipeImageBlock)
admin_site.register(RecipeTextBlock)
admin_site.register(RecipeTimerBlock)

