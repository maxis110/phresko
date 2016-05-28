import json
from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError


class BaseManager(models.Manager):


    def filter_by_list(self, params, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        for name in params.keys():
            args = {'%s__in' % name: params[name]}
            queryset = queryset.filter(**args)
        return queryset

    def search(self, value, queryset=None):
        model = self.model
        if value is not None and value != '' and model.search_args:
            kwargs = []
            for arg in model.search_args:
                if arg in model._meta.get_all_field_names():
                    field = model._meta.get_field_by_name(arg)[0]
                    try:
                        field.to_python(value)
                    except ValidationError:
                        continue
                    
                kwargs.append({arg : value})
            filter_query = [Q(**kwarg) for kwarg in kwargs]
            if not filter_query:
                queryset = model.objects.none()
            else:
                queryset = self.filter(reduce(lambda q1, q2: q1|q2, filter_query))
        return queryset

    def get(self, *args, **kwargs):
        instance = super(BaseManager, self).get(*args, **kwargs)
        return instance

    def all(self, *args, **kwargs):
        queryset = super(BaseManager, self).all(*args, **kwargs)
        return queryset

    def filter(self, *args, **kwargs):
        queryset = super(BaseManager, self).filter(*args, **kwargs)
        return queryset

    def get_queryset(self, *args, **kwargs):
        return super(BaseManager, self).get_queryset(*args, **kwargs)

    def raw(self, *args, **kwargs):
        return super(BaseManager, self).raw(*args, **kwargs)

    def own(self, queryset=None):
        return self.all() if queryset is None else queryset.all()
