# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class FrameworkSortOrder(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, direction: str=None, _field: str=None):
        """FrameworkSortOrder - a model defined in OpenAPI

        :param direction: The direction of this FrameworkSortOrder.
        :param _field: The _field of this FrameworkSortOrder.
        """
        self.openapi_types = {
            'direction': str,
            '_field': str
        }

        self.attribute_map = {
            'direction': 'direction',
            '_field': 'field'
        }

        self._direction = direction
        self.__field = _field

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FrameworkSortOrder':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The framework-sort-order of this FrameworkSortOrder.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def direction(self):
        """Gets the direction of this FrameworkSortOrder.

        Sorting direction.

        :return: The direction of this FrameworkSortOrder.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this FrameworkSortOrder.

        Sorting direction.

        :param direction: The direction of this FrameworkSortOrder.
        :type direction: str
        """
        if direction is None:
            raise ValueError("Invalid value for `direction`, must not be `None`")

        self._direction = direction

    @property
    def _field(self):
        """Gets the _field of this FrameworkSortOrder.

        Sorting field.

        :return: The _field of this FrameworkSortOrder.
        :rtype: str
        """
        return self.__field

    @_field.setter
    def _field(self, _field):
        """Sets the _field of this FrameworkSortOrder.

        Sorting field.

        :param _field: The _field of this FrameworkSortOrder.
        :type _field: str
        """
        if _field is None:
            raise ValueError("Invalid value for `_field`, must not be `None`")

        self.__field = _field
