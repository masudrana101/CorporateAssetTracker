import django_filters
from django_filters.rest_framework import FilterSet
from .models import UserAccount as User

class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']