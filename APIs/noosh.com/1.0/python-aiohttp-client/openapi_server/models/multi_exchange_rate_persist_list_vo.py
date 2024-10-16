# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.multi_exchange_rate_persisit_vo import MultiExchangeRatePersisitVO
from openapi_server import util


class MultiExchangeRatePersistListVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, exchange_rates: List[MultiExchangeRatePersisitVO]=None):
        """MultiExchangeRatePersistListVO - a model defined in OpenAPI

        :param exchange_rates: The exchange_rates of this MultiExchangeRatePersistListVO.
        """
        self.openapi_types = {
            'exchange_rates': List[MultiExchangeRatePersisitVO]
        }

        self.attribute_map = {
            'exchange_rates': 'exchange_rates'
        }

        self._exchange_rates = exchange_rates

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MultiExchangeRatePersistListVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MultiExchangeRatePersistListVO of this MultiExchangeRatePersistListVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def exchange_rates(self):
        """Gets the exchange_rates of this MultiExchangeRatePersistListVO.

        

        :return: The exchange_rates of this MultiExchangeRatePersistListVO.
        :rtype: List[MultiExchangeRatePersisitVO]
        """
        return self._exchange_rates

    @exchange_rates.setter
    def exchange_rates(self, exchange_rates):
        """Sets the exchange_rates of this MultiExchangeRatePersistListVO.

        

        :param exchange_rates: The exchange_rates of this MultiExchangeRatePersistListVO.
        :type exchange_rates: List[MultiExchangeRatePersisitVO]
        """

        self._exchange_rates = exchange_rates
