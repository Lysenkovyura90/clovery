
from .models import Task

import django_filters


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = '__all__'
