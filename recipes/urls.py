from rest_framework import routers

from recipes.views import RecipesViewSet

router = routers.SimpleRouter()
router.register('', RecipesViewSet)
urlpatterns = router.urls
