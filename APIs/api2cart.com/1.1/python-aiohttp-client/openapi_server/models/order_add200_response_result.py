# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OrderAdd200ResponseResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, order_id: str=None):
        """OrderAdd200ResponseResult - a model defined in OpenAPI

        :param order_id: The order_id of this OrderAdd200ResponseResult.
        """
        self.openapi_types = {
            'order_id': str
        }

        self.attribute_map = {
            'order_id': 'order_id'
        }

        self._order_id = order_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OrderAdd200ResponseResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OrderAdd_200_response_result of this OrderAdd200ResponseResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def order_id(self):
        """Gets the order_id of this OrderAdd200ResponseResult.


        :return: The order_id of this OrderAdd200ResponseResult.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderAdd200ResponseResult.


        :param order_id: The order_id of this OrderAdd200ResponseResult.
        :type order_id: str
        """

        self._order_id = order_id
