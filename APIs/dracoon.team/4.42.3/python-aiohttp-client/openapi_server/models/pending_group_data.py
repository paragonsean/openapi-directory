# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PendingGroupData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None):
        """PendingGroupData - a model defined in OpenAPI

        :param id: The id of this PendingGroupData.
        :param name: The name of this PendingGroupData.
        """
        self.openapi_types = {
            'id': int,
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name'
        }

        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PendingGroupData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PendingGroupData of this PendingGroupData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this PendingGroupData.

        Unique identifier for the group  use `id` from `GroupInfo` instead

        :return: The id of this PendingGroupData.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PendingGroupData.

        Unique identifier for the group  use `id` from `GroupInfo` instead

        :param id: The id of this PendingGroupData.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this PendingGroupData.

        Group name  use `name` from `GroupInfo` instead

        :return: The name of this PendingGroupData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PendingGroupData.

        Group name  use `name` from `GroupInfo` instead

        :param name: The name of this PendingGroupData.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
