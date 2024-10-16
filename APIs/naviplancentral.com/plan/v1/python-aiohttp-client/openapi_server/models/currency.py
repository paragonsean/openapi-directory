# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Currency(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, formatted_decimal: str=None, formatted_no_decimal: str=None, raw: float=None):
        """Currency - a model defined in OpenAPI

        :param formatted_decimal: The formatted_decimal of this Currency.
        :param formatted_no_decimal: The formatted_no_decimal of this Currency.
        :param raw: The raw of this Currency.
        """
        self.openapi_types = {
            'formatted_decimal': str,
            'formatted_no_decimal': str,
            'raw': float
        }

        self.attribute_map = {
            'formatted_decimal': 'formattedDecimal',
            'formatted_no_decimal': 'formattedNoDecimal',
            'raw': 'raw'
        }

        self._formatted_decimal = formatted_decimal
        self._formatted_no_decimal = formatted_no_decimal
        self._raw = raw

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Currency':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Currency of this Currency.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def formatted_decimal(self):
        """Gets the formatted_decimal of this Currency.


        :return: The formatted_decimal of this Currency.
        :rtype: str
        """
        return self._formatted_decimal

    @formatted_decimal.setter
    def formatted_decimal(self, formatted_decimal):
        """Sets the formatted_decimal of this Currency.


        :param formatted_decimal: The formatted_decimal of this Currency.
        :type formatted_decimal: str
        """

        self._formatted_decimal = formatted_decimal

    @property
    def formatted_no_decimal(self):
        """Gets the formatted_no_decimal of this Currency.


        :return: The formatted_no_decimal of this Currency.
        :rtype: str
        """
        return self._formatted_no_decimal

    @formatted_no_decimal.setter
    def formatted_no_decimal(self, formatted_no_decimal):
        """Sets the formatted_no_decimal of this Currency.


        :param formatted_no_decimal: The formatted_no_decimal of this Currency.
        :type formatted_no_decimal: str
        """

        self._formatted_no_decimal = formatted_no_decimal

    @property
    def raw(self):
        """Gets the raw of this Currency.


        :return: The raw of this Currency.
        :rtype: float
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this Currency.


        :param raw: The raw of this Currency.
        :type raw: float
        """

        self._raw = raw
