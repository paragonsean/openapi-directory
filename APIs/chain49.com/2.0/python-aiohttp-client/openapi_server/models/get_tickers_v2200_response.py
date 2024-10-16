# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetTickersV2200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, rates: object=None, ts: int=None):
        """GetTickersV2200Response - a model defined in OpenAPI

        :param rates: The rates of this GetTickersV2200Response.
        :param ts: The ts of this GetTickersV2200Response.
        """
        self.openapi_types = {
            'rates': object,
            'ts': int
        }

        self.attribute_map = {
            'rates': 'rates',
            'ts': 'ts'
        }

        self._rates = rates
        self._ts = ts

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetTickersV2200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getTickersV2_200_response of this GetTickersV2200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rates(self):
        """Gets the rates of this GetTickersV2200Response.


        :return: The rates of this GetTickersV2200Response.
        :rtype: object
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this GetTickersV2200Response.


        :param rates: The rates of this GetTickersV2200Response.
        :type rates: object
        """

        self._rates = rates

    @property
    def ts(self):
        """Gets the ts of this GetTickersV2200Response.


        :return: The ts of this GetTickersV2200Response.
        :rtype: int
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this GetTickersV2200Response.


        :param ts: The ts of this GetTickersV2200Response.
        :type ts: int
        """

        self._ts = ts
