# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ProductOptionAdd200ResponseResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, option_id: str=None, product_option_id: str=None):
        """ProductOptionAdd200ResponseResult - a model defined in OpenAPI

        :param option_id: The option_id of this ProductOptionAdd200ResponseResult.
        :param product_option_id: The product_option_id of this ProductOptionAdd200ResponseResult.
        """
        self.openapi_types = {
            'option_id': str,
            'product_option_id': str
        }

        self.attribute_map = {
            'option_id': 'option_id',
            'product_option_id': 'product_option_id'
        }

        self._option_id = option_id
        self._product_option_id = product_option_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProductOptionAdd200ResponseResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProductOptionAdd_200_response_result of this ProductOptionAdd200ResponseResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def option_id(self):
        """Gets the option_id of this ProductOptionAdd200ResponseResult.


        :return: The option_id of this ProductOptionAdd200ResponseResult.
        :rtype: str
        """
        return self._option_id

    @option_id.setter
    def option_id(self, option_id):
        """Sets the option_id of this ProductOptionAdd200ResponseResult.


        :param option_id: The option_id of this ProductOptionAdd200ResponseResult.
        :type option_id: str
        """

        self._option_id = option_id

    @property
    def product_option_id(self):
        """Gets the product_option_id of this ProductOptionAdd200ResponseResult.


        :return: The product_option_id of this ProductOptionAdd200ResponseResult.
        :rtype: str
        """
        return self._product_option_id

    @product_option_id.setter
    def product_option_id(self, product_option_id):
        """Sets the product_option_id of this ProductOptionAdd200ResponseResult.


        :param product_option_id: The product_option_id of this ProductOptionAdd200ResponseResult.
        :type product_option_id: str
        """

        self._product_option_id = product_option_id
