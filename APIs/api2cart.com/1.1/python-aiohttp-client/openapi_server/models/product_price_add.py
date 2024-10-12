# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.product_add_group_prices_inner import ProductAddGroupPricesInner
from openapi_server import util


class ProductPriceAdd(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, group_prices: List[ProductAddGroupPricesInner]=None, product_id: str=None):
        """ProductPriceAdd - a model defined in OpenAPI

        :param group_prices: The group_prices of this ProductPriceAdd.
        :param product_id: The product_id of this ProductPriceAdd.
        """
        self.openapi_types = {
            'group_prices': List[ProductAddGroupPricesInner],
            'product_id': str
        }

        self.attribute_map = {
            'group_prices': 'group_prices',
            'product_id': 'product_id'
        }

        self._group_prices = group_prices
        self._product_id = product_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProductPriceAdd':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProductPriceAdd of this ProductPriceAdd.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def group_prices(self):
        """Gets the group_prices of this ProductPriceAdd.

        Defines product's group prices

        :return: The group_prices of this ProductPriceAdd.
        :rtype: List[ProductAddGroupPricesInner]
        """
        return self._group_prices

    @group_prices.setter
    def group_prices(self, group_prices):
        """Sets the group_prices of this ProductPriceAdd.

        Defines product's group prices

        :param group_prices: The group_prices of this ProductPriceAdd.
        :type group_prices: List[ProductAddGroupPricesInner]
        """

        self._group_prices = group_prices

    @property
    def product_id(self):
        """Gets the product_id of this ProductPriceAdd.

        Defines the product to which the price has to be added

        :return: The product_id of this ProductPriceAdd.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductPriceAdd.

        Defines the product to which the price has to be added

        :param product_id: The product_id of this ProductPriceAdd.
        :type product_id: str
        """

        self._product_id = product_id
