from django.http import HttpResponse
from rest_framework import status
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Pokemon, Ability, Pokemon_Ability
from .serializers import PokemonSerializer, AbilitySerializer, PokemonAbilityResponseSerializer, PokemonAbilityCreateSerializer


# Create your views here.

def index(request):
    return HttpResponse("Страница приложения pokemons")


class PokemonViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class AbilityViewSet(ModelViewSet):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer


class PokemonAbilityViewSet(ModelViewSet):
    queryset = Pokemon_Ability.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return PokemonAbilityCreateSerializer
        return PokemonAbilityResponseSerializer

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PUT")

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PATCH")

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pokemon_ability = serializer.save()

        response_serializer = PokemonAbilityResponseSerializer(pokemon_ability)
        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PokemonAbilityAddView(APIView):
    def post(self, request):
        pokemon_id = request.data.get('pokemon')
        ability_id = request.data.get('ability')

        # Проверка, существуют ли Pokemon и Ability с переданными ID
        pokemon = get_object_or_404(Pokemon, id=pokemon_id)
        ability = get_object_or_404(Ability, id=ability_id)

        # Создание записи в таблице Pokemon_Ability
        pokemon_ability = Pokemon_Ability.objects.create(pokemon=pokemon, ability=ability)

        # Сериализация и возврат данных
        response_serializer = PokemonAbilityResponseSerializer(pokemon_ability)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
