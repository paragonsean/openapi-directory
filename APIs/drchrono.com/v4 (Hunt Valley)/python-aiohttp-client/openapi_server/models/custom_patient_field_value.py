# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CustomPatientFieldValue(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, field_type: int=None, updated_at: str=None, value: str=None):
        """CustomPatientFieldValue - a model defined in OpenAPI

        :param field_type: The field_type of this CustomPatientFieldValue.
        :param updated_at: The updated_at of this CustomPatientFieldValue.
        :param value: The value of this CustomPatientFieldValue.
        """
        self.openapi_types = {
            'field_type': int,
            'updated_at': str,
            'value': str
        }

        self.attribute_map = {
            'field_type': 'field_type',
            'updated_at': 'updated_at',
            'value': 'value'
        }

        self._field_type = field_type
        self._updated_at = updated_at
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CustomPatientFieldValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CustomPatientFieldValue of this CustomPatientFieldValue.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def field_type(self):
        """Gets the field_type of this CustomPatientFieldValue.

        ID of the `/api/custom_demographics` object

        :return: The field_type of this CustomPatientFieldValue.
        :rtype: int
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this CustomPatientFieldValue.

        ID of the `/api/custom_demographics` object

        :param field_type: The field_type of this CustomPatientFieldValue.
        :type field_type: int
        """

        self._field_type = field_type

    @property
    def updated_at(self):
        """Gets the updated_at of this CustomPatientFieldValue.

        

        :return: The updated_at of this CustomPatientFieldValue.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CustomPatientFieldValue.

        

        :param updated_at: The updated_at of this CustomPatientFieldValue.
        :type updated_at: str
        """

        self._updated_at = updated_at

    @property
    def value(self):
        """Gets the value of this CustomPatientFieldValue.

        

        :return: The value of this CustomPatientFieldValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomPatientFieldValue.

        

        :param value: The value of this CustomPatientFieldValue.
        :type value: str
        """

        self._value = value
