# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetDetailedRefundsIn(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, country_codes: str=None, date_from: str=None, date_to: str=None, format: str=None, limit: float=None, offset: float=None):
        """GetDetailedRefundsIn - a model defined in OpenAPI

        :param country_codes: The country_codes of this GetDetailedRefundsIn.
        :param date_from: The date_from of this GetDetailedRefundsIn.
        :param date_to: The date_to of this GetDetailedRefundsIn.
        :param format: The format of this GetDetailedRefundsIn.
        :param limit: The limit of this GetDetailedRefundsIn.
        :param offset: The offset of this GetDetailedRefundsIn.
        """
        self.openapi_types = {
            'country_codes': str,
            'date_from': str,
            'date_to': str,
            'format': str,
            'limit': float,
            'offset': float
        }

        self.attribute_map = {
            'country_codes': 'country_codes',
            'date_from': 'date_from',
            'date_to': 'date_to',
            'format': 'format',
            'limit': 'limit',
            'offset': 'offset'
        }

        self._country_codes = country_codes
        self._date_from = date_from
        self._date_to = date_to
        self._format = format
        self._limit = limit
        self._offset = offset

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetDetailedRefundsIn':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getDetailedRefundsIn of this GetDetailedRefundsIn.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def country_codes(self):
        """Gets the country_codes of this GetDetailedRefundsIn.

        Comma separated list of 2-letter country codes

        :return: The country_codes of this GetDetailedRefundsIn.
        :rtype: str
        """
        return self._country_codes

    @country_codes.setter
    def country_codes(self, country_codes):
        """Sets the country_codes of this GetDetailedRefundsIn.

        Comma separated list of 2-letter country codes

        :param country_codes: The country_codes of this GetDetailedRefundsIn.
        :type country_codes: str
        """

        self._country_codes = country_codes

    @property
    def date_from(self):
        """Gets the date_from of this GetDetailedRefundsIn.

        Take only refunds issued at or after the date. Format: yyyy-MM-dd

        :return: The date_from of this GetDetailedRefundsIn.
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this GetDetailedRefundsIn.

        Take only refunds issued at or after the date. Format: yyyy-MM-dd

        :param date_from: The date_from of this GetDetailedRefundsIn.
        :type date_from: str
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """Gets the date_to of this GetDetailedRefundsIn.

        Take only refunds issued at or before the date. Format: yyyy-MM-dd

        :return: The date_to of this GetDetailedRefundsIn.
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """Sets the date_to of this GetDetailedRefundsIn.

        Take only refunds issued at or before the date. Format: yyyy-MM-dd

        :param date_to: The date_to of this GetDetailedRefundsIn.
        :type date_to: str
        """

        self._date_to = date_to

    @property
    def format(self):
        """Gets the format of this GetDetailedRefundsIn.

        Output format. 'json' or 'csv'. Default value is 'json'

        :return: The format of this GetDetailedRefundsIn.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this GetDetailedRefundsIn.

        Output format. 'json' or 'csv'. Default value is 'json'

        :param format: The format of this GetDetailedRefundsIn.
        :type format: str
        """

        self._format = format

    @property
    def limit(self):
        """Gets the limit of this GetDetailedRefundsIn.

        Limit (no more than 1000, defaults to 100).

        :return: The limit of this GetDetailedRefundsIn.
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this GetDetailedRefundsIn.

        Limit (no more than 1000, defaults to 100).

        :param limit: The limit of this GetDetailedRefundsIn.
        :type limit: float
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this GetDetailedRefundsIn.

        Offset. Defaults to 0

        :return: The offset of this GetDetailedRefundsIn.
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this GetDetailedRefundsIn.

        Offset. Defaults to 0

        :param offset: The offset of this GetDetailedRefundsIn.
        :type offset: float
        """

        self._offset = offset
