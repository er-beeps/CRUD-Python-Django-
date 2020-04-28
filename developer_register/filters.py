import django_filters
from django_filters import CharFilter
from .models import *

class DeveloperFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name = 'first_name' , lookup_expr = 'icontains')
    last_name = CharFilter(field_name = 'last_name' , lookup_expr = 'icontains')
    email = CharFilter(field_name='email' , lookup_expr = 'icontains')
    experirence = CharFilter(field_name = 'experirence' , lookup_expr = 'icontains')
    class Meta:
        model = Developer
        fields = '__all__'
        exclude = ['gender', 'mobile', 'image','remarks']
        

