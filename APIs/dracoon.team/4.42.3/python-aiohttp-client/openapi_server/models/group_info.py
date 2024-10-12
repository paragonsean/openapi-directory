# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GroupInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None):
        """GroupInfo - a model defined in OpenAPI

        :param id: The id of this GroupInfo.
        :param name: The name of this GroupInfo.
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
    def from_dict(cls, dikt: dict) -> 'GroupInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GroupInfo of this GroupInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this GroupInfo.

        Unique identifier for the group

        :return: The id of this GroupInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupInfo.

        Unique identifier for the group

        :param id: The id of this GroupInfo.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this GroupInfo.

        Group name

        :return: The name of this GroupInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupInfo.

        Group name

        :param name: The name of this GroupInfo.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
