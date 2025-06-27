from abc import ABC, ABCMeta
from typing import Type

DOUBLE_UNDERLINE = '__'

class ModelMeta(Type):
    def __new__(cls, name, bases, attrs):
        fields = {}
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith(DOUBLE_UNDERLINE):
                fields[attr_name] = attr_value
        attrs["_fields"] = fields
        new_class = super().__new__(cls, name, bases, attrs)
        return new_class

class CombinatedMeta(ModelMeta, ABCMeta):
    pass

class Model(ABC, metaclass=CombinatedMeta):
    def __init__(self, **kwargs):
        for field_name in self._fields:
            setattr(self, field_name, kwargs.get(field_name, self._fields[field_name]))

    def __repr__(self):
        field_values = ", ".join(f"{field}={getattr(self, field)}" for field in self._fields)
        return f"{self.__class__.__name__}({field_values})"

    def to_dict(self):
      return {field: getattr(self, field) for field in self._fields}