# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ProfilesInnerStatistics(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, connections: float=None):
        """ProfilesInnerStatistics - a model defined in OpenAPI

        :param connections: The connections of this ProfilesInnerStatistics.
        """
        self.openapi_types = {
            'connections': float
        }

        self.attribute_map = {
            'connections': 'connections'
        }

        self._connections = connections

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProfilesInnerStatistics':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The profiles_inner_statistics of this ProfilesInnerStatistics.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def connections(self):
        """Gets the connections of this ProfilesInnerStatistics.


        :return: The connections of this ProfilesInnerStatistics.
        :rtype: float
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this ProfilesInnerStatistics.


        :param connections: The connections of this ProfilesInnerStatistics.
        :type connections: float
        """

        self._connections = connections
