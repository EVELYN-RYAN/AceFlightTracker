import django_filters
from .models import *

class IncompleteFilter(django_filters.FilterSet):
    class Meta:
        model = Flight
        fields = '__all__'
        