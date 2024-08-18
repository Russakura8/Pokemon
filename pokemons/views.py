from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from rest_framework.viewsets import ModelViewSet

from .models import Pokemon, Ability, Pokemon_Ability
from .serializers import PokemonSerializer, AbilitySerializer


# Create your views here.

def index(request):
    return HttpResponse("Страница приложения pokemons")


class PokemonViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class AbilityViewSet(ModelViewSet):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer

