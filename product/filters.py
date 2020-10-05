import django_filters
from .models import Color,Category,Type,creator
from product.models import Product



class ColorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',)
    class Meta:
        model = Color
        fields ='__all__'


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Category
        fields ='__all__'


class TypeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Type
        fields ='__all__'


class creatorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = creator
        fields ='__all__'

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields ='__all__'
        exclude = ('img','priceIn','quantity','active',)
