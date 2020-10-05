import django_filters
from .models import Employe,Absense



class EmployeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',)
    address = django_filters.CharFilter(lookup_expr='icontains',)
    telephone = django_filters.CharFilter(lookup_expr='icontains',)
    salary = django_filters.CharFilter(lookup_expr='icontains',)
    class Meta:
        model = Employe
        fields ='__all__'

class AbsenseFilter(django_filters.FilterSet):
    class Meta:
        model = Absense
        fields =('name','date')