import requests

from django.shortcuts import render
from django.db.models import Max, Avg

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import CharacterRating


class CharacterViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response({'error': 'not id for character'})

    def retrieve(self, request, pk=None):
        URL = f"https://swapi.dev/api/people/{pk}"
        json_response = requests.get(URL).json()
        return Response({
            "name": json_response['name'],
            "height": json_response['height'],
            "mass": json_response['mass'],
            "hair_color": json_response['hair_color'],
            "skin_color": json_response['skin_color'],
            "eye_color": json_response['eye_color'],
            "birth_year": json_response['birth_year'],
            "gender": json_response['gender'],
            "homeworld": self.get_homeworld(json_response['homeworld']),
            "species": self.get_species(json_response['species']),
            "average_rating": self.get_average_rating(id=pk),
            "max_rating": self.get_max_rating(id=pk),
        })

    def get_homeworld(self, url):
        try:
            response = requests.get(url)
            hw = response.json()
            return {
                "name": hw['name'],
                "population": hw['population'],
                "known_residents_count": len(hw['residents']),
            }
        except:
            return {}
    
    def get_species(self, url):
        try:
            response = requests.get(url[0])
            species = response.json()
            return species['name']
        except:
            return ''

    def get_max_rating(self, id):
        character = CharacterRating.objects.filter(character_id=id) \
                                           .aggregate(Max('rating'))
        return character['rating__max'] if character['rating__max'] else ''
        
    def get_average_rating(self, id):
        character =  CharacterRating.objects.filter(character_id=id) \
                                            .aggregate(Avg('rating'))
        return character['rating__avg'] if character['rating__avg'] else ''


@api_view(['POST'], )
def create_rating(request, id):
    rating = getattr(request, "rating", 0)
    if request.method == 'POST' and id and check(rating):
        CharacterRating.objects.create(character_id=id, 
                                       rating=rating)
        return Response({"message": "Successful!"})
    return Response({"message": "Error!"})

def check(rating):
    return True if int(rating) in [1,2,3,4,5] else False