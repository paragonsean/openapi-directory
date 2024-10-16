# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.field_filters_inner_any_of import FieldFiltersInnerAnyOf
from openapi_server.models.field_filters_inner_any_of1 import FieldFiltersInnerAnyOf1
from openapi_server import util


class FieldFiltersInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, param: str=None):
        """FieldFiltersInner - a model defined in OpenAPI

        :param name: The name of this FieldFiltersInner.
        :param param: The param of this FieldFiltersInner.
        """
        self.openapi_types = {
            'name': str,
            'param': str
        }

        self.attribute_map = {
            'name': 'name',
            'param': 'param'
        }

        self._name = name
        self._param = param

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FieldFiltersInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The field_filters_inner of this FieldFiltersInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this FieldFiltersInner.


        :return: The name of this FieldFiltersInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FieldFiltersInner.


        :param name: The name of this FieldFiltersInner.
        :type name: str
        """

        self._name = name

    @property
    def param(self):
        """Gets the param of this FieldFiltersInner.


        :return: The param of this FieldFiltersInner.
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this FieldFiltersInner.


        :param param: The param of this FieldFiltersInner.
        :type param: str
        """

        self._param = param
