from django_filters import rest_framework as filters
from logistic.models import Product, Stock, StockProduct


class StockFilter(filters.FilterSet):
    address = filters.CharFilter(field_name='address', lookup_expr='icontains')

    class Meta:
        model = Stock
        fields = ['address']