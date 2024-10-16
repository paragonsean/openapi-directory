# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UserDefinedFieldDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, category_type_id: int=None, description: str=None, id: int=None, order_index: int=None):
        """UserDefinedFieldDto - a model defined in OpenAPI

        :param category_type_id: The category_type_id of this UserDefinedFieldDto.
        :param description: The description of this UserDefinedFieldDto.
        :param id: The id of this UserDefinedFieldDto.
        :param order_index: The order_index of this UserDefinedFieldDto.
        """
        self.openapi_types = {
            'category_type_id': int,
            'description': str,
            'id': int,
            'order_index': int
        }

        self.attribute_map = {
            'category_type_id': 'categoryTypeId',
            'description': 'description',
            'id': 'id',
            'order_index': 'orderIndex'
        }

        self._category_type_id = category_type_id
        self._description = description
        self._id = id
        self._order_index = order_index

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserDefinedFieldDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserDefinedFieldDto of this UserDefinedFieldDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def category_type_id(self):
        """Gets the category_type_id of this UserDefinedFieldDto.


        :return: The category_type_id of this UserDefinedFieldDto.
        :rtype: int
        """
        return self._category_type_id

    @category_type_id.setter
    def category_type_id(self, category_type_id):
        """Sets the category_type_id of this UserDefinedFieldDto.


        :param category_type_id: The category_type_id of this UserDefinedFieldDto.
        :type category_type_id: int
        """

        self._category_type_id = category_type_id

    @property
    def description(self):
        """Gets the description of this UserDefinedFieldDto.


        :return: The description of this UserDefinedFieldDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserDefinedFieldDto.


        :param description: The description of this UserDefinedFieldDto.
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this UserDefinedFieldDto.


        :return: The id of this UserDefinedFieldDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDefinedFieldDto.


        :param id: The id of this UserDefinedFieldDto.
        :type id: int
        """

        self._id = id

    @property
    def order_index(self):
        """Gets the order_index of this UserDefinedFieldDto.


        :return: The order_index of this UserDefinedFieldDto.
        :rtype: int
        """
        return self._order_index

    @order_index.setter
    def order_index(self, order_index):
        """Sets the order_index of this UserDefinedFieldDto.


        :param order_index: The order_index of this UserDefinedFieldDto.
        :type order_index: int
        """

        self._order_index = order_index
