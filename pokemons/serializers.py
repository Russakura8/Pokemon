from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from pokemons.models import Pokemon, Ability, Pokemon_Ability


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'


class AbilitySerializer(ModelSerializer):
    class Meta:
        model = Ability
        fields = '__all__'


class PokemonAbilityCreateSerializer(serializers.Serializer):
    pokemon_name = serializers.CharField(max_length=100)
    HP = serializers.IntegerField()
    length = serializers.FloatField()
    weight = serializers.FloatField()
    species = serializers.CharField(max_length=100)
    pokemon_element = serializers.ChoiceField(choices=Pokemon.Element.choices)
    rarity = serializers.ChoiceField(choices=Pokemon.Rarity.choices)
    other = serializers.CharField(max_length=255, allow_blank=True)
    ability_name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    cost = serializers.IntegerField()
    ability_element = serializers.ChoiceField(choices=Ability.Element.choices)

    def create(self, validated_data):
        # Извлечение данных для моделей Pokemon и Ability
        pokemon_data = {
            'pokemon_name': validated_data['pokemon_name'],
            'HP': validated_data['HP'],
            'length': validated_data['length'],
            'weight': validated_data['weight'],
            'species': validated_data['species'],
            'pokemon_element': validated_data['pokemon_element'],
            'rarity': validated_data['rarity'],
            'other': validated_data['other'],
        }
        ability_data = {
            'ability_name': validated_data['ability_name'],
            'description': validated_data['description'],
            'cost': validated_data['cost'],
            'ability_element': validated_data['ability_element'],
        }

        # Создание Pokemon и Ability
        pokemon = Pokemon.objects.create(**pokemon_data)
        ability = Ability.objects.create(**ability_data)

        # Создание связи в Pokemon_Ability
        pokemon_ability = Pokemon_Ability.objects.create(pokemon=pokemon, ability=ability)

        return pokemon_ability


class PokemonAbilityResponseSerializer(serializers.ModelSerializer):
    pokemon_name = serializers.CharField(source='pokemon.pokemon_name')
    HP = serializers.IntegerField(source='pokemon.HP')
    length = serializers.FloatField(source='pokemon.length')
    weight = serializers.FloatField(source='pokemon.weight')
    species = serializers.CharField(source='pokemon.species')
    pokemon_element = serializers.CharField(source='pokemon.pokemon_element')
    rarity = serializers.CharField(source='pokemon.rarity')
    other = serializers.CharField(source='pokemon.other', allow_blank=True)
    ability_name = serializers.CharField(source='ability.ability_name')
    description = serializers.CharField(source='ability.description')
    cost = serializers.IntegerField(source='ability.cost')
    ability_element = serializers.CharField(source='ability.ability_element')

    class Meta:
        model = Pokemon_Ability
        fields = (
            'pokemon_name', 'HP', 'length', 'weight', 'species', 'pokemon_element',
            'rarity', 'other', 'ability_name', 'description', 'cost', 'ability_element'
        )
