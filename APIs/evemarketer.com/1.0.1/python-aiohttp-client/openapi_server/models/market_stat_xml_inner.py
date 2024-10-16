# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.type_stat_xml import TypeStatXML
from openapi_server import util


class MarketStatXMLInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, buy: TypeStatXML=None, sell: TypeStatXML=None):
        """MarketStatXMLInner - a model defined in OpenAPI

        :param buy: The buy of this MarketStatXMLInner.
        :param sell: The sell of this MarketStatXMLInner.
        """
        self.openapi_types = {
            'buy': TypeStatXML,
            'sell': TypeStatXML
        }

        self.attribute_map = {
            'buy': 'buy',
            'sell': 'sell'
        }

        self._buy = buy
        self._sell = sell

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MarketStatXMLInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MarketStatXML_inner of this MarketStatXMLInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def buy(self):
        """Gets the buy of this MarketStatXMLInner.


        :return: The buy of this MarketStatXMLInner.
        :rtype: TypeStatXML
        """
        return self._buy

    @buy.setter
    def buy(self, buy):
        """Sets the buy of this MarketStatXMLInner.


        :param buy: The buy of this MarketStatXMLInner.
        :type buy: TypeStatXML
        """

        self._buy = buy

    @property
    def sell(self):
        """Gets the sell of this MarketStatXMLInner.


        :return: The sell of this MarketStatXMLInner.
        :rtype: TypeStatXML
        """
        return self._sell

    @sell.setter
    def sell(self, sell):
        """Sets the sell of this MarketStatXMLInner.


        :param sell: The sell of this MarketStatXMLInner.
        :type sell: TypeStatXML
        """

        self._sell = sell
