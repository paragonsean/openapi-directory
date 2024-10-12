# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OrderRefundAddItemsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, order_product_id: str=None, price: float=None, quantity: int=None):
        """OrderRefundAddItemsInner - a model defined in OpenAPI

        :param order_product_id: The order_product_id of this OrderRefundAddItemsInner.
        :param price: The price of this OrderRefundAddItemsInner.
        :param quantity: The quantity of this OrderRefundAddItemsInner.
        """
        self.openapi_types = {
            'order_product_id': str,
            'price': float,
            'quantity': int
        }

        self.attribute_map = {
            'order_product_id': 'order_product_id',
            'price': 'price',
            'quantity': 'quantity'
        }

        self._order_product_id = order_product_id
        self._price = price
        self._quantity = quantity

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OrderRefundAddItemsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OrderRefundAdd_items_inner of this OrderRefundAddItemsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def order_product_id(self):
        """Gets the order_product_id of this OrderRefundAddItemsInner.


        :return: The order_product_id of this OrderRefundAddItemsInner.
        :rtype: str
        """
        return self._order_product_id

    @order_product_id.setter
    def order_product_id(self, order_product_id):
        """Sets the order_product_id of this OrderRefundAddItemsInner.


        :param order_product_id: The order_product_id of this OrderRefundAddItemsInner.
        :type order_product_id: str
        """

        self._order_product_id = order_product_id

    @property
    def price(self):
        """Gets the price of this OrderRefundAddItemsInner.


        :return: The price of this OrderRefundAddItemsInner.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderRefundAddItemsInner.


        :param price: The price of this OrderRefundAddItemsInner.
        :type price: float
        """

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this OrderRefundAddItemsInner.


        :return: The quantity of this OrderRefundAddItemsInner.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderRefundAddItemsInner.


        :param quantity: The quantity of this OrderRefundAddItemsInner.
        :type quantity: int
        """

        self._quantity = quantity
