import django_filters
from .models import Color,Category,Type,creator
from product.models import Order, Product



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
        exclude = ('img','priceIn','quantity','active','barcode_IMG')

class OrderFilter(django_filters.FilterSet):
    order_date = django_filters.DateFromToRangeFilter(field_name='order_date',)  
    class Meta:
        model = Order
        fields ='__all__'
        exclude=('ordered')

class Order2Filter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields =('user','emp')

        
