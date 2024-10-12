# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OrderAddOrderItemInnerOrderItemPropertyInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, order_item_property_name: str=None, order_item_property_value: str=None):
        """OrderAddOrderItemInnerOrderItemPropertyInner - a model defined in OpenAPI

        :param order_item_property_name: The order_item_property_name of this OrderAddOrderItemInnerOrderItemPropertyInner.
        :param order_item_property_value: The order_item_property_value of this OrderAddOrderItemInnerOrderItemPropertyInner.
        """
        self.openapi_types = {
            'order_item_property_name': str,
            'order_item_property_value': str
        }

        self.attribute_map = {
            'order_item_property_name': 'order_item_property_name',
            'order_item_property_value': 'order_item_property_value'
        }

        self._order_item_property_name = order_item_property_name
        self._order_item_property_value = order_item_property_value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OrderAddOrderItemInnerOrderItemPropertyInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OrderAdd_order_item_inner_order_item_property_inner of this OrderAddOrderItemInnerOrderItemPropertyInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def order_item_property_name(self):
        """Gets the order_item_property_name of this OrderAddOrderItemInnerOrderItemPropertyInner.

        Ordered product property name. Where x is order item ID, y is order item property ID

        :return: The order_item_property_name of this OrderAddOrderItemInnerOrderItemPropertyInner.
        :rtype: str
        """
        return self._order_item_property_name

    @order_item_property_name.setter
    def order_item_property_name(self, order_item_property_name):
        """Sets the order_item_property_name of this OrderAddOrderItemInnerOrderItemPropertyInner.

        Ordered product property name. Where x is order item ID, y is order item property ID

        :param order_item_property_name: The order_item_property_name of this OrderAddOrderItemInnerOrderItemPropertyInner.
        :type order_item_property_name: str
        """

        self._order_item_property_name = order_item_property_name

    @property
    def order_item_property_value(self):
        """Gets the order_item_property_value of this OrderAddOrderItemInnerOrderItemPropertyInner.

        Ordered product property value. Where x is order item ID, y - order item property ID

        :return: The order_item_property_value of this OrderAddOrderItemInnerOrderItemPropertyInner.
        :rtype: str
        """
        return self._order_item_property_value

    @order_item_property_value.setter
    def order_item_property_value(self, order_item_property_value):
        """Sets the order_item_property_value of this OrderAddOrderItemInnerOrderItemPropertyInner.

        Ordered product property value. Where x is order item ID, y - order item property ID

        :param order_item_property_value: The order_item_property_value of this OrderAddOrderItemInnerOrderItemPropertyInner.
        :type order_item_property_value: str
        """

        self._order_item_property_value = order_item_property_value
