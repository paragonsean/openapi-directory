# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ElementaryPrice(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount: str=None, currency_code: str=None):
        """ElementaryPrice - a model defined in OpenAPI

        :param amount: The amount of this ElementaryPrice.
        :param currency_code: The currency_code of this ElementaryPrice.
        """
        self.openapi_types = {
            'amount': str,
            'currency_code': str
        }

        self.attribute_map = {
            'amount': 'amount',
            'currency_code': 'currencyCode'
        }

        self._amount = amount
        self._currency_code = currency_code

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ElementaryPrice':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ElementaryPrice of this ElementaryPrice.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self):
        """Gets the amount of this ElementaryPrice.

        Amount of the fare. could be alpha numeric. Ex- 500.20 or 514.13A, 'A'signifies additional collection.

        :return: The amount of this ElementaryPrice.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ElementaryPrice.

        Amount of the fare. could be alpha numeric. Ex- 500.20 or 514.13A, 'A'signifies additional collection.

        :param amount: The amount of this ElementaryPrice.
        :type amount: str
        """

        self._amount = amount

    @property
    def currency_code(self):
        """Gets the currency_code of this ElementaryPrice.

        Currency type of the fare.

        :return: The currency_code of this ElementaryPrice.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this ElementaryPrice.

        Currency type of the fare.

        :param currency_code: The currency_code of this ElementaryPrice.
        :type currency_code: str
        """

        self._currency_code = currency_code
