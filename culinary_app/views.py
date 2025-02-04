from rest_framework import viewsets, permissions
from .serializers import ChefSerializer, DishSerializer, IngredientSerializer, RatingSerializer
from .models import Chef, Dish, Ingredient, Rating


class ChefViewSet(viewsets.ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
    permission_classes = [permissions.IsAuthenticated]

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]