from django.db import models


"""
class Character(models.Model):
    name = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    mass = models.CharField(max_length=100)
    hair_color = models.CharField(max_length=100)
    skin_color = models.CharField(max_length=100)
    eye_color = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    homeworld = models.CharField(max_length=100)
    species_name = models.CharField(max_length=100)
"""


class CharacterRating(models.Model):
    character_id = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()