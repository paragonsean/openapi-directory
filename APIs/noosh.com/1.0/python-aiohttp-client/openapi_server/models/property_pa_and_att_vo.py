# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PropertyPaAndAttVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, date_value: date=None, number_value: object=None, param_id: int=None, param_name: str=None, property_attribute_id: int=None, string_value: str=None):
        """PropertyPaAndAttVO - a model defined in OpenAPI

        :param date_value: The date_value of this PropertyPaAndAttVO.
        :param number_value: The number_value of this PropertyPaAndAttVO.
        :param param_id: The param_id of this PropertyPaAndAttVO.
        :param param_name: The param_name of this PropertyPaAndAttVO.
        :param property_attribute_id: The property_attribute_id of this PropertyPaAndAttVO.
        :param string_value: The string_value of this PropertyPaAndAttVO.
        """
        self.openapi_types = {
            'date_value': date,
            'number_value': object,
            'param_id': int,
            'param_name': str,
            'property_attribute_id': int,
            'string_value': str
        }

        self.attribute_map = {
            'date_value': 'date_value',
            'number_value': 'number_value',
            'param_id': 'param_id',
            'param_name': 'param_name',
            'property_attribute_id': 'property_attribute_id',
            'string_value': 'string_value'
        }

        self._date_value = date_value
        self._number_value = number_value
        self._param_id = param_id
        self._param_name = param_name
        self._property_attribute_id = property_attribute_id
        self._string_value = string_value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PropertyPaAndAttVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PropertyPaAndAttVO of this PropertyPaAndAttVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def date_value(self):
        """Gets the date_value of this PropertyPaAndAttVO.

        

        :return: The date_value of this PropertyPaAndAttVO.
        :rtype: date
        """
        return self._date_value

    @date_value.setter
    def date_value(self, date_value):
        """Sets the date_value of this PropertyPaAndAttVO.

        

        :param date_value: The date_value of this PropertyPaAndAttVO.
        :type date_value: date
        """

        self._date_value = date_value

    @property
    def number_value(self):
        """Gets the number_value of this PropertyPaAndAttVO.

        Java type: java.math.BigDecimal

        :return: The number_value of this PropertyPaAndAttVO.
        :rtype: object
        """
        return self._number_value

    @number_value.setter
    def number_value(self, number_value):
        """Sets the number_value of this PropertyPaAndAttVO.

        Java type: java.math.BigDecimal

        :param number_value: The number_value of this PropertyPaAndAttVO.
        :type number_value: object
        """

        self._number_value = number_value

    @property
    def param_id(self):
        """Gets the param_id of this PropertyPaAndAttVO.

        

        :return: The param_id of this PropertyPaAndAttVO.
        :rtype: int
        """
        return self._param_id

    @param_id.setter
    def param_id(self, param_id):
        """Sets the param_id of this PropertyPaAndAttVO.

        

        :param param_id: The param_id of this PropertyPaAndAttVO.
        :type param_id: int
        """

        self._param_id = param_id

    @property
    def param_name(self):
        """Gets the param_name of this PropertyPaAndAttVO.

        

        :return: The param_name of this PropertyPaAndAttVO.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        """Sets the param_name of this PropertyPaAndAttVO.

        

        :param param_name: The param_name of this PropertyPaAndAttVO.
        :type param_name: str
        """

        self._param_name = param_name

    @property
    def property_attribute_id(self):
        """Gets the property_attribute_id of this PropertyPaAndAttVO.

        

        :return: The property_attribute_id of this PropertyPaAndAttVO.
        :rtype: int
        """
        return self._property_attribute_id

    @property_attribute_id.setter
    def property_attribute_id(self, property_attribute_id):
        """Sets the property_attribute_id of this PropertyPaAndAttVO.

        

        :param property_attribute_id: The property_attribute_id of this PropertyPaAndAttVO.
        :type property_attribute_id: int
        """

        self._property_attribute_id = property_attribute_id

    @property
    def string_value(self):
        """Gets the string_value of this PropertyPaAndAttVO.

        

        :return: The string_value of this PropertyPaAndAttVO.
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value):
        """Sets the string_value of this PropertyPaAndAttVO.

        

        :param string_value: The string_value of this PropertyPaAndAttVO.
        :type string_value: str
        """

        self._string_value = string_value
