from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *


router = SimpleRouter()

router.register(r'pokemon', PokemonViewSet)
router.register(r'ability', AbilityViewSet)

urlpatterns = [
    path('', index),
]

urlpatterns += router.urls