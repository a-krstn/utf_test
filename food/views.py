from django.db.models import Prefetch, Count, Q
from rest_framework.generics import ListAPIView

from .models import FoodCategory, Food
from .serializers import FoodListSerializer


class FoodAPIList(ListAPIView):
    queryset = ((FoodCategory.objects.prefetch_related(Prefetch('food',
                                                                queryset=Food.objects.filter(is_publish=True).
                                                                prefetch_related('additional'))).
                annotate(published=Count('food', filter=Q(food__is_publish=True)))).
                filter(published__gt=0))
    serializer_class = FoodListSerializer
