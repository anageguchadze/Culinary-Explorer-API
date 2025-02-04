from rest_framework import serializers
from .models import *

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class DishSerializer(serializers.ModelSerializer):
    chef = ChefSerializer()
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Dish
        fields = '__all__'

class RatingtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'