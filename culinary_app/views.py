from rest_framework import viewsets, permissions
from .serializers import ChefSerializer, DishSerializer, IngredientSerializer, RatingSerializer
from .models import Chef, Dish, Ingredient, Rating
from .filters import DishFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


class ChefViewSet(viewsets.ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
    permission_classes = [permissions.IsAuthenticated]

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend] 
    filterset_class = DishFilter

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def recommended_dishes(request):
    user = request.user

    # მომხმარებლის ყველაზე მაღალი შეფასებული კერძები
    top_rated = Rating.objects.filter(user=user).order_by('-score')[:5]

    # ინგრედიენტების ამოღება მომხმარებლისთვის საყვარელი კერძებიდან
    favorite_ingredients = []
    for rating in top_rated:
        favorite_ingredients.extend(rating.dish.ingredients.values_list('name', flat=True))

    # რეკომენდაციის ალგორითმი: კერძები მსგავს ინგრედიენტებზე დაყრდნობით
    recommendations = Dish.objects.filter(
        ingredients__name__in=favorite_ingredients
    ).exclude(
        ratings__user=user  # არ გამოვაჩინოთ უკვე შეფასებული კერძები
    ).annotate(
        avg_rating=Avg('ratings__score')
    ).order_by('-avg_rating')[:10]  # ტოპ 10 რეკომენდაცია

    serializer = DishSerializer(recommendations, many=True)
    return Response(serializer.data)