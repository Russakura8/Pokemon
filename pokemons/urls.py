from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *


router = SimpleRouter()

router.register(r'pokemon', PokemonViewSet)
router.register(r'ability', AbilityViewSet)
router.register(r'pokemon_ability', PokemonAbilityViewSet, basename='pokemon_ability')

urlpatterns = [
    path('', index),
    path('pokemon_ability_add/', PokemonAbilityAddView.as_view(), name='pokemon_ability_add'),
]

urlpatterns += router.urls