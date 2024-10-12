# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ProductVariantUpdateOptionsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, option_name: str=None, option_value: str=None):
        """ProductVariantUpdateOptionsInner - a model defined in OpenAPI

        :param option_name: The option_name of this ProductVariantUpdateOptionsInner.
        :param option_value: The option_value of this ProductVariantUpdateOptionsInner.
        """
        self.openapi_types = {
            'option_name': str,
            'option_value': str
        }

        self.attribute_map = {
            'option_name': 'option_name',
            'option_value': 'option_value'
        }

        self._option_name = option_name
        self._option_value = option_value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProductVariantUpdateOptionsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProductVariantUpdate_options_inner of this ProductVariantUpdateOptionsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def option_name(self):
        """Gets the option_name of this ProductVariantUpdateOptionsInner.


        :return: The option_name of this ProductVariantUpdateOptionsInner.
        :rtype: str
        """
        return self._option_name

    @option_name.setter
    def option_name(self, option_name):
        """Sets the option_name of this ProductVariantUpdateOptionsInner.


        :param option_name: The option_name of this ProductVariantUpdateOptionsInner.
        :type option_name: str
        """

        self._option_name = option_name

    @property
    def option_value(self):
        """Gets the option_value of this ProductVariantUpdateOptionsInner.


        :return: The option_value of this ProductVariantUpdateOptionsInner.
        :rtype: str
        """
        return self._option_value

    @option_value.setter
    def option_value(self, option_value):
        """Sets the option_value of this ProductVariantUpdateOptionsInner.


        :param option_value: The option_value of this ProductVariantUpdateOptionsInner.
        :type option_value: str
        """

        self._option_value = option_value
