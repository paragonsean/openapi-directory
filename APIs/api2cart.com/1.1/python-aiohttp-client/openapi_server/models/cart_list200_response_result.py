# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.cart_list200_response_result_supported_carts_inner import CartList200ResponseResultSupportedCartsInner
from openapi_server import util


class CartList200ResponseResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, supported_carts: List[CartList200ResponseResultSupportedCartsInner]=None):
        """CartList200ResponseResult - a model defined in OpenAPI

        :param supported_carts: The supported_carts of this CartList200ResponseResult.
        """
        self.openapi_types = {
            'supported_carts': List[CartList200ResponseResultSupportedCartsInner]
        }

        self.attribute_map = {
            'supported_carts': 'supported_carts'
        }

        self._supported_carts = supported_carts

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CartList200ResponseResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CartList_200_response_result of this CartList200ResponseResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def supported_carts(self):
        """Gets the supported_carts of this CartList200ResponseResult.


        :return: The supported_carts of this CartList200ResponseResult.
        :rtype: List[CartList200ResponseResultSupportedCartsInner]
        """
        return self._supported_carts

    @supported_carts.setter
    def supported_carts(self, supported_carts):
        """Sets the supported_carts of this CartList200ResponseResult.


        :param supported_carts: The supported_carts of this CartList200ResponseResult.
        :type supported_carts: List[CartList200ResponseResultSupportedCartsInner]
        """

        self._supported_carts = supported_carts
