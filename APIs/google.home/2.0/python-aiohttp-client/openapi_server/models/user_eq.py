# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.high_shelf import HighShelf
from openapi_server.models.low_shelf import LowShelf
from openapi_server import util


class UserEq(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, high_shelf: HighShelf=None, low_shelf: LowShelf=None, max_peaking_eqs: int=None, peaking_eqs: List[str]=None):
        """UserEq - a model defined in OpenAPI

        :param high_shelf: The high_shelf of this UserEq.
        :param low_shelf: The low_shelf of this UserEq.
        :param max_peaking_eqs: The max_peaking_eqs of this UserEq.
        :param peaking_eqs: The peaking_eqs of this UserEq.
        """
        self.openapi_types = {
            'high_shelf': HighShelf,
            'low_shelf': LowShelf,
            'max_peaking_eqs': int,
            'peaking_eqs': List[str]
        }

        self.attribute_map = {
            'high_shelf': 'high_shelf',
            'low_shelf': 'low_shelf',
            'max_peaking_eqs': 'max_peaking_eqs',
            'peaking_eqs': 'peaking_eqs'
        }

        self._high_shelf = high_shelf
        self._low_shelf = low_shelf
        self._max_peaking_eqs = max_peaking_eqs
        self._peaking_eqs = peaking_eqs

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserEq':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserEq of this UserEq.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def high_shelf(self):
        """Gets the high_shelf of this UserEq.


        :return: The high_shelf of this UserEq.
        :rtype: HighShelf
        """
        return self._high_shelf

    @high_shelf.setter
    def high_shelf(self, high_shelf):
        """Sets the high_shelf of this UserEq.


        :param high_shelf: The high_shelf of this UserEq.
        :type high_shelf: HighShelf
        """
        if high_shelf is None:
            raise ValueError("Invalid value for `high_shelf`, must not be `None`")

        self._high_shelf = high_shelf

    @property
    def low_shelf(self):
        """Gets the low_shelf of this UserEq.


        :return: The low_shelf of this UserEq.
        :rtype: LowShelf
        """
        return self._low_shelf

    @low_shelf.setter
    def low_shelf(self, low_shelf):
        """Sets the low_shelf of this UserEq.


        :param low_shelf: The low_shelf of this UserEq.
        :type low_shelf: LowShelf
        """
        if low_shelf is None:
            raise ValueError("Invalid value for `low_shelf`, must not be `None`")

        self._low_shelf = low_shelf

    @property
    def max_peaking_eqs(self):
        """Gets the max_peaking_eqs of this UserEq.


        :return: The max_peaking_eqs of this UserEq.
        :rtype: int
        """
        return self._max_peaking_eqs

    @max_peaking_eqs.setter
    def max_peaking_eqs(self, max_peaking_eqs):
        """Sets the max_peaking_eqs of this UserEq.


        :param max_peaking_eqs: The max_peaking_eqs of this UserEq.
        :type max_peaking_eqs: int
        """
        if max_peaking_eqs is None:
            raise ValueError("Invalid value for `max_peaking_eqs`, must not be `None`")

        self._max_peaking_eqs = max_peaking_eqs

    @property
    def peaking_eqs(self):
        """Gets the peaking_eqs of this UserEq.


        :return: The peaking_eqs of this UserEq.
        :rtype: List[str]
        """
        return self._peaking_eqs

    @peaking_eqs.setter
    def peaking_eqs(self, peaking_eqs):
        """Sets the peaking_eqs of this UserEq.


        :param peaking_eqs: The peaking_eqs of this UserEq.
        :type peaking_eqs: List[str]
        """
        if peaking_eqs is None:
            raise ValueError("Invalid value for `peaking_eqs`, must not be `None`")

        self._peaking_eqs = peaking_eqs
