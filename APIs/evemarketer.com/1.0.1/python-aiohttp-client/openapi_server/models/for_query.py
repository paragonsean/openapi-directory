# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ForQuery(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bid: bool=None, hours: int=None, minq: int=None, regions: List[int]=None, systems: List[int]=None, types: List[int]=None):
        """ForQuery - a model defined in OpenAPI

        :param bid: The bid of this ForQuery.
        :param hours: The hours of this ForQuery.
        :param minq: The minq of this ForQuery.
        :param regions: The regions of this ForQuery.
        :param systems: The systems of this ForQuery.
        :param types: The types of this ForQuery.
        """
        self.openapi_types = {
            'bid': bool,
            'hours': int,
            'minq': int,
            'regions': List[int],
            'systems': List[int],
            'types': List[int]
        }

        self.attribute_map = {
            'bid': 'bid',
            'hours': 'hours',
            'minq': 'minq',
            'regions': 'regions',
            'systems': 'systems',
            'types': 'types'
        }

        self._bid = bid
        self._hours = hours
        self._minq = minq
        self._regions = regions
        self._systems = systems
        self._types = types

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ForQuery':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ForQuery of this ForQuery.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bid(self):
        """Gets the bid of this ForQuery.

        is buy?

        :return: The bid of this ForQuery.
        :rtype: bool
        """
        return self._bid

    @bid.setter
    def bid(self, bid):
        """Sets the bid of this ForQuery.

        is buy?

        :param bid: The bid of this ForQuery.
        :type bid: bool
        """

        self._bid = bid

    @property
    def hours(self):
        """Gets the hours of this ForQuery.

        always 0

        :return: The hours of this ForQuery.
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this ForQuery.

        always 0

        :param hours: The hours of this ForQuery.
        :type hours: int
        """

        self._hours = hours

    @property
    def minq(self):
        """Gets the minq of this ForQuery.

        always 0

        :return: The minq of this ForQuery.
        :rtype: int
        """
        return self._minq

    @minq.setter
    def minq(self, minq):
        """Sets the minq of this ForQuery.

        always 0

        :param minq: The minq of this ForQuery.
        :type minq: int
        """

        self._minq = minq

    @property
    def regions(self):
        """Gets the regions of this ForQuery.

        Region IDs

        :return: The regions of this ForQuery.
        :rtype: List[int]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ForQuery.

        Region IDs

        :param regions: The regions of this ForQuery.
        :type regions: List[int]
        """

        self._regions = regions

    @property
    def systems(self):
        """Gets the systems of this ForQuery.

        System IDs

        :return: The systems of this ForQuery.
        :rtype: List[int]
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """Sets the systems of this ForQuery.

        System IDs

        :param systems: The systems of this ForQuery.
        :type systems: List[int]
        """

        self._systems = systems

    @property
    def types(self):
        """Gets the types of this ForQuery.

        Type IDs

        :return: The types of this ForQuery.
        :rtype: List[int]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this ForQuery.

        Type IDs

        :param types: The types of this ForQuery.
        :type types: List[int]
        """

        self._types = types
