import django_filters
from .models import Dish

class DishFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  
    chef__user__username = django_filters.CharFilter(lookup_expr='icontains')  
    ingredients__name = django_filters.CharFilter(lookup_expr='icontains')  
    min_rating = django_filters.NumberFilter(field_name='ratings__score', lookup_expr='gte')  

    class Meta:
        model = Dish
        fields = ['name', 'chef__user__username', 'ingredients__name', 'min_rating']
