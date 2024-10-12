# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.types_with_id_types_type_inner import TypesWithIdTypesTypeInner
from openapi_server import util


class TypesWithIdTypes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type: List[TypesWithIdTypesTypeInner]=None):
        """TypesWithIdTypes - a model defined in OpenAPI

        :param type: The type of this TypesWithIdTypes.
        """
        self.openapi_types = {
            'type': List[TypesWithIdTypesTypeInner]
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TypesWithIdTypes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The types_with_id_types of this TypesWithIdTypes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this TypesWithIdTypes.


        :return: The type of this TypesWithIdTypes.
        :rtype: List[TypesWithIdTypesTypeInner]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TypesWithIdTypes.


        :param type: The type of this TypesWithIdTypes.
        :type type: List[TypesWithIdTypesTypeInner]
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        if type is not None and len(type) < 1:
            raise ValueError("Invalid value for `type`, number of items must be greater than or equal to `1`")

        self._type = type
