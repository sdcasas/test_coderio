from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.character.views import CharacterViewSet, create_rating


urlpatterns = [
    path(r'<int:id>/rating', create_rating)
]

router = SimpleRouter()
router.register(r'', CharacterViewSet, basename="character")

urlpatterns += router.urls