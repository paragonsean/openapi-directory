# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BuildsListToolsets200ResponseNodeInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current: bool=None, name: str=None):
        """BuildsListToolsets200ResponseNodeInner - a model defined in OpenAPI

        :param current: The current of this BuildsListToolsets200ResponseNodeInner.
        :param name: The name of this BuildsListToolsets200ResponseNodeInner.
        """
        self.openapi_types = {
            'current': bool,
            'name': str
        }

        self.attribute_map = {
            'current': 'current',
            'name': 'name'
        }

        self._current = current
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BuildsListToolsets200ResponseNodeInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The builds_listToolsets_200_response_node_inner of this BuildsListToolsets200ResponseNodeInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current(self):
        """Gets the current of this BuildsListToolsets200ResponseNodeInner.

        If the Node version is default for AppCenter

        :return: The current of this BuildsListToolsets200ResponseNodeInner.
        :rtype: bool
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this BuildsListToolsets200ResponseNodeInner.

        If the Node version is default for AppCenter

        :param current: The current of this BuildsListToolsets200ResponseNodeInner.
        :type current: bool
        """

        self._current = current

    @property
    def name(self):
        """Gets the name of this BuildsListToolsets200ResponseNodeInner.

        The version name

        :return: The name of this BuildsListToolsets200ResponseNodeInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BuildsListToolsets200ResponseNodeInner.

        The version name

        :param name: The name of this BuildsListToolsets200ResponseNodeInner.
        :type name: str
        """

        self._name = name
