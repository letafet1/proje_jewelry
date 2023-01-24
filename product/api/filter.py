import django_filters
from product.models import *

class ProductFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(lookup_expr='icontains')
    category__title=django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields=['category','name','category__title']