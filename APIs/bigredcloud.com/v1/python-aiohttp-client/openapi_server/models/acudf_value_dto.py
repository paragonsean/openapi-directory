# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AcudfValueDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, id: int=None, user_defined_field_id: int=None, value: str=None):
        """AcudfValueDto - a model defined in OpenAPI

        :param description: The description of this AcudfValueDto.
        :param id: The id of this AcudfValueDto.
        :param user_defined_field_id: The user_defined_field_id of this AcudfValueDto.
        :param value: The value of this AcudfValueDto.
        """
        self.openapi_types = {
            'description': str,
            'id': int,
            'user_defined_field_id': int,
            'value': str
        }

        self.attribute_map = {
            'description': 'description',
            'id': 'id',
            'user_defined_field_id': 'userDefinedFieldId',
            'value': 'value'
        }

        self._description = description
        self._id = id
        self._user_defined_field_id = user_defined_field_id
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AcudfValueDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AcudfValueDto of this AcudfValueDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this AcudfValueDto.


        :return: The description of this AcudfValueDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AcudfValueDto.


        :param description: The description of this AcudfValueDto.
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this AcudfValueDto.


        :return: The id of this AcudfValueDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AcudfValueDto.


        :param id: The id of this AcudfValueDto.
        :type id: int
        """

        self._id = id

    @property
    def user_defined_field_id(self):
        """Gets the user_defined_field_id of this AcudfValueDto.


        :return: The user_defined_field_id of this AcudfValueDto.
        :rtype: int
        """
        return self._user_defined_field_id

    @user_defined_field_id.setter
    def user_defined_field_id(self, user_defined_field_id):
        """Sets the user_defined_field_id of this AcudfValueDto.


        :param user_defined_field_id: The user_defined_field_id of this AcudfValueDto.
        :type user_defined_field_id: int
        """

        self._user_defined_field_id = user_defined_field_id

    @property
    def value(self):
        """Gets the value of this AcudfValueDto.


        :return: The value of this AcudfValueDto.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AcudfValueDto.


        :param value: The value of this AcudfValueDto.
        :type value: str
        """

        self._value = value
