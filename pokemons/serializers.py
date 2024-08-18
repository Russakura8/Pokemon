from rest_framework.serializers import ModelSerializer

from pokemons.models import Pokemon, Ability


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'


class AbilitySerializer(ModelSerializer):
    class Meta:
        model = Ability
        fields = '__all__'

