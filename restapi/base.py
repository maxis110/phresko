from django.conf import settings
from django.db import models
from django.forms.models import model_to_dict
import json
from rest_framework.exceptions import APIException
from copy import deepcopy
from rest_framework import status


def dict_as_json(data):
    assert isinstance(data, dict)
    values = {}
    for key, value in data.items():
        values[key] = value
    return json.dumps(values)


class BaseModel(models.Model):
    search_args = ()
    actions = []

    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)

    def is_own(self):
        if self.pk is None:
            return True
        return bool(self.__class__.objects.filter(pk=self.pk))

    def save_raw(self, *args, **kwargs):
        return super(BaseModel, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        return super(BaseModel, self).save(*args, **kwargs)

    def delete(self):
        return super(BaseModel, self).delete()

    class Meta:
        abstract = True