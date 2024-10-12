# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.catalog_data_special_price_interface import CatalogDataSpecialPriceInterface
from openapi_server import util


class CatalogSpecialPriceStorageV1UpdatePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, prices: List[CatalogDataSpecialPriceInterface]=None):
        """CatalogSpecialPriceStorageV1UpdatePostRequest - a model defined in OpenAPI

        :param prices: The prices of this CatalogSpecialPriceStorageV1UpdatePostRequest.
        """
        self.openapi_types = {
            'prices': List[CatalogDataSpecialPriceInterface]
        }

        self.attribute_map = {
            'prices': 'prices'
        }

        self._prices = prices

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CatalogSpecialPriceStorageV1UpdatePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The catalogSpecialPriceStorageV1UpdatePost_request of this CatalogSpecialPriceStorageV1UpdatePostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def prices(self):
        """Gets the prices of this CatalogSpecialPriceStorageV1UpdatePostRequest.


        :return: The prices of this CatalogSpecialPriceStorageV1UpdatePostRequest.
        :rtype: List[CatalogDataSpecialPriceInterface]
        """
        return self._prices

    @prices.setter
    def prices(self, prices):
        """Sets the prices of this CatalogSpecialPriceStorageV1UpdatePostRequest.


        :param prices: The prices of this CatalogSpecialPriceStorageV1UpdatePostRequest.
        :type prices: List[CatalogDataSpecialPriceInterface]
        """
        if prices is None:
            raise ValueError("Invalid value for `prices`, must not be `None`")

        self._prices = prices
