import django_filters
from .models import trunkenlace


class TrunkenlaFilter(django_filters.FilterSet):
    class Meta:
        model = trunkenlace
        fields = ['num_trunke', 'num_enlatr', 'num_dnenla', 'num_dnlin' ]