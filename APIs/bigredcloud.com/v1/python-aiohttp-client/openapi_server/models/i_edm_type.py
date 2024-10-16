# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class IEdmType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type_kind: int=None):
        """IEdmType - a model defined in OpenAPI

        :param type_kind: The type_kind of this IEdmType.
        """
        self.openapi_types = {
            'type_kind': int
        }

        self.attribute_map = {
            'type_kind': 'TypeKind'
        }

        self._type_kind = type_kind

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IEdmType':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IEdmType of this IEdmType.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type_kind(self):
        """Gets the type_kind of this IEdmType.


        :return: The type_kind of this IEdmType.
        :rtype: int
        """
        return self._type_kind

    @type_kind.setter
    def type_kind(self, type_kind):
        """Sets the type_kind of this IEdmType.


        :param type_kind: The type_kind of this IEdmType.
        :type type_kind: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7]  # noqa: E501
        if type_kind not in allowed_values:
            raise ValueError(
                "Invalid value for `type_kind` ({0}), must be one of {1}"
                .format(type_kind, allowed_values)
            )

        self._type_kind = type_kind
