from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import DishViewSet, ChefViewSet, IngredientViewSet, RatingViewSet, recommended_dishes
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('dishes', DishViewSet)
router.register('chefs', ChefViewSet)
router.register('ingredients', IngredientViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('recommendations/', recommended_dishes, name='recommended-dishes'),
]
