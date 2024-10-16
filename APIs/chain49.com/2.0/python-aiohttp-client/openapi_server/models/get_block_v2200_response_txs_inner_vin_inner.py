# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetBlockV2200ResponseTxsInnerVinInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, is_address: bool=None, n: int=None, value: str=None):
        """GetBlockV2200ResponseTxsInnerVinInner - a model defined in OpenAPI

        :param is_address: The is_address of this GetBlockV2200ResponseTxsInnerVinInner.
        :param n: The n of this GetBlockV2200ResponseTxsInnerVinInner.
        :param value: The value of this GetBlockV2200ResponseTxsInnerVinInner.
        """
        self.openapi_types = {
            'is_address': bool,
            'n': int,
            'value': str
        }

        self.attribute_map = {
            'is_address': 'isAddress',
            'n': 'n',
            'value': 'value'
        }

        self._is_address = is_address
        self._n = n
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetBlockV2200ResponseTxsInnerVinInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getBlockV2_200_response_txs_inner_vin_inner of this GetBlockV2200ResponseTxsInnerVinInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def is_address(self):
        """Gets the is_address of this GetBlockV2200ResponseTxsInnerVinInner.


        :return: The is_address of this GetBlockV2200ResponseTxsInnerVinInner.
        :rtype: bool
        """
        return self._is_address

    @is_address.setter
    def is_address(self, is_address):
        """Sets the is_address of this GetBlockV2200ResponseTxsInnerVinInner.


        :param is_address: The is_address of this GetBlockV2200ResponseTxsInnerVinInner.
        :type is_address: bool
        """

        self._is_address = is_address

    @property
    def n(self):
        """Gets the n of this GetBlockV2200ResponseTxsInnerVinInner.


        :return: The n of this GetBlockV2200ResponseTxsInnerVinInner.
        :rtype: int
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this GetBlockV2200ResponseTxsInnerVinInner.


        :param n: The n of this GetBlockV2200ResponseTxsInnerVinInner.
        :type n: int
        """

        self._n = n

    @property
    def value(self):
        """Gets the value of this GetBlockV2200ResponseTxsInnerVinInner.


        :return: The value of this GetBlockV2200ResponseTxsInnerVinInner.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GetBlockV2200ResponseTxsInnerVinInner.


        :param value: The value of this GetBlockV2200ResponseTxsInnerVinInner.
        :type value: str
        """

        self._value = value
