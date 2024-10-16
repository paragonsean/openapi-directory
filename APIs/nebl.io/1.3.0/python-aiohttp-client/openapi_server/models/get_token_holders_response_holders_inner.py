# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetTokenHoldersResponseHoldersInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address: str=None, amount: float=None):
        """GetTokenHoldersResponseHoldersInner - a model defined in OpenAPI

        :param address: The address of this GetTokenHoldersResponseHoldersInner.
        :param amount: The amount of this GetTokenHoldersResponseHoldersInner.
        """
        self.openapi_types = {
            'address': str,
            'amount': float
        }

        self.attribute_map = {
            'address': 'address',
            'amount': 'amount'
        }

        self._address = address
        self._amount = amount

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetTokenHoldersResponseHoldersInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getTokenHoldersResponse_holders_inner of this GetTokenHoldersResponseHoldersInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this GetTokenHoldersResponseHoldersInner.


        :return: The address of this GetTokenHoldersResponseHoldersInner.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this GetTokenHoldersResponseHoldersInner.


        :param address: The address of this GetTokenHoldersResponseHoldersInner.
        :type address: str
        """

        self._address = address

    @property
    def amount(self):
        """Gets the amount of this GetTokenHoldersResponseHoldersInner.


        :return: The amount of this GetTokenHoldersResponseHoldersInner.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetTokenHoldersResponseHoldersInner.


        :param amount: The amount of this GetTokenHoldersResponseHoldersInner.
        :type amount: float
        """

        self._amount = amount
