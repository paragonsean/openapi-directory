# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.i_restricted_stock import IRestrictedStock
from openapi_server.models.object_link import ObjectLink
from openapi_server import util


class RestrictedStocksModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, links: List[ObjectLink]=None, restricted_stocks: List[IRestrictedStock]=None):
        """RestrictedStocksModel - a model defined in OpenAPI

        :param links: The links of this RestrictedStocksModel.
        :param restricted_stocks: The restricted_stocks of this RestrictedStocksModel.
        """
        self.openapi_types = {
            'links': List[ObjectLink],
            'restricted_stocks': List[IRestrictedStock]
        }

        self.attribute_map = {
            'links': 'links',
            'restricted_stocks': 'restrictedStocks'
        }

        self._links = links
        self._restricted_stocks = restricted_stocks

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RestrictedStocksModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RestrictedStocksModel of this RestrictedStocksModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self):
        """Gets the links of this RestrictedStocksModel.


        :return: The links of this RestrictedStocksModel.
        :rtype: List[ObjectLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RestrictedStocksModel.


        :param links: The links of this RestrictedStocksModel.
        :type links: List[ObjectLink]
        """

        self._links = links

    @property
    def restricted_stocks(self):
        """Gets the restricted_stocks of this RestrictedStocksModel.


        :return: The restricted_stocks of this RestrictedStocksModel.
        :rtype: List[IRestrictedStock]
        """
        return self._restricted_stocks

    @restricted_stocks.setter
    def restricted_stocks(self, restricted_stocks):
        """Sets the restricted_stocks of this RestrictedStocksModel.


        :param restricted_stocks: The restricted_stocks of this RestrictedStocksModel.
        :type restricted_stocks: List[IRestrictedStock]
        """

        self._restricted_stocks = restricted_stocks
