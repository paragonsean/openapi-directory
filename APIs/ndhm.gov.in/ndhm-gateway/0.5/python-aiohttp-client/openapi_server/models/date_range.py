# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DateRange(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _from: datetime=None, to: datetime=None):
        """DateRange - a model defined in OpenAPI

        :param _from: The _from of this DateRange.
        :param to: The to of this DateRange.
        """
        self.openapi_types = {
            '_from': datetime,
            'to': datetime
        }

        self.attribute_map = {
            '_from': 'from',
            'to': 'to'
        }

        self.__from = _from
        self._to = to

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DateRange':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The dateRange of this DateRange.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _from(self):
        """Gets the _from of this DateRange.


        :return: The _from of this DateRange.
        :rtype: datetime
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this DateRange.


        :param _from: The _from of this DateRange.
        :type _from: datetime
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this DateRange.


        :return: The to of this DateRange.
        :rtype: datetime
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this DateRange.


        :param to: The to of this DateRange.
        :type to: datetime
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")

        self._to = to
