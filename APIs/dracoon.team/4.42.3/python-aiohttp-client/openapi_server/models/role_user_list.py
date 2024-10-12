# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.range import Range
from openapi_server.models.role_user import RoleUser
from openapi_server import util


class RoleUserList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, items: List[RoleUser]=None, range: Range=None):
        """RoleUserList - a model defined in OpenAPI

        :param items: The items of this RoleUserList.
        :param range: The range of this RoleUserList.
        """
        self.openapi_types = {
            'items': List[RoleUser],
            'range': Range
        }

        self.attribute_map = {
            'items': 'items',
            'range': 'range'
        }

        self._items = items
        self._range = range

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RoleUserList':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RoleUserList of this RoleUserList.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self):
        """Gets the items of this RoleUserList.

        List of role-user mappings

        :return: The items of this RoleUserList.
        :rtype: List[RoleUser]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this RoleUserList.

        List of role-user mappings

        :param items: The items of this RoleUserList.
        :type items: List[RoleUser]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items

    @property
    def range(self):
        """Gets the range of this RoleUserList.


        :return: The range of this RoleUserList.
        :rtype: Range
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this RoleUserList.


        :param range: The range of this RoleUserList.
        :type range: Range
        """
        if range is None:
            raise ValueError("Invalid value for `range`, must not be `None`")

        self._range = range
