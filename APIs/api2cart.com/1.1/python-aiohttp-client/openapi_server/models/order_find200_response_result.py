# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.order import Order
from openapi_server import util


class OrderFind200ResponseResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, order: List[Order]=None):
        """OrderFind200ResponseResult - a model defined in OpenAPI

        :param order: The order of this OrderFind200ResponseResult.
        """
        self.openapi_types = {
            'order': List[Order]
        }

        self.attribute_map = {
            'order': 'order'
        }

        self._order = order

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OrderFind200ResponseResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OrderFind_200_response_result of this OrderFind200ResponseResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def order(self):
        """Gets the order of this OrderFind200ResponseResult.


        :return: The order of this OrderFind200ResponseResult.
        :rtype: List[Order]
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this OrderFind200ResponseResult.


        :param order: The order of this OrderFind200ResponseResult.
        :type order: List[Order]
        """

        self._order = order
