from django.db import models
from django.utils.translation import gettext_lazy as _


class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=100)
    HP = models.IntegerField()
    length = models.FloatField()
    weight = models.FloatField()
    species = models.CharField(max_length=100)

    class Element(models.TextChoices):
        GRASS = 'GR', _('Grass')
        FIRE = 'FR', _('Fire')
        WATER = 'WA', _('Water')
        LIGHTNING = 'LI', _('Lightning')
        FIGHTING = 'FT', _('Fighting')
        PSYCHIC = 'PS', _('Psychic')
        COLORLESS = 'CL', _('Colorless')
        DARKNESS = 'DA', _('Darkness')
        METAL = 'ME', _('Metal')
        DRAGON = 'DR', _('Dragon')
        FAIRY = 'FA', _('Fairy')
        UNKNOWN = 'UN', _('Unknown')

    pokemon_element = models.CharField(max_length=2, choices=Element.choices, default=Element.UNKNOWN)

    class Rarity(models.TextChoices):
        COMMON = 'CO', _('Common')
        UNCOMMON = 'UN', _('Uncommon')
        RARE = 'RA', _('Rare')
        PROMO = 'PR', _('Promo')

    rarity = models.CharField(max_length=2, choices=Rarity.choices, default=Rarity.COMMON)

    other = models.TextField(blank=True)


class Ability(models.Model):
    ability_name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.IntegerField()

    class Element(models.TextChoices):
        GRASS = 'GR', _('Grass')
        FIRE = 'FR', _('Fire')
        WATER = 'WA', _('Water')
        LIGHTNING = 'LI', _('Lightning')
        FIGHTING = 'FT', _('Fighting')
        PSYCHIC = 'PS', _('Psychic')
        COLORLESS = 'CL', _('Colorless')
        DARKNESS = 'DA', _('Darkness')
        METAL = 'ME', _('Metal')
        DRAGON = 'DR', _('Dragon')
        FAIRY = 'FA', _('Fairy')
        UNKNOWN = 'UN', _('Unknown')

    ability_element = models.CharField(max_length=2, choices=Element.choices, default=Element.UNKNOWN)


class Pokemon_Ability(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    firts_ability = models.ForeignKey(Ability, on_delete=models.CASCADE, related_name="first_ability")
    second_ability = models.ForeignKey(Ability, on_delete=models.CASCADE, related_name="second_ability")
