# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.count_of import CountOf
from openapi_server import util


class ProductsApiCount200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None):
        """ProductsApiCount200Response - a model defined in OpenAPI

        :param count: The count of this ProductsApiCount200Response.
        """
        self.openapi_types = {
            'count': int
        }

        self.attribute_map = {
            'count': 'count'
        }

        self._count = count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProductsApiCount200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProductsApi_Count_200_response of this ProductsApiCount200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this ProductsApiCount200Response.


        :return: The count of this ProductsApiCount200Response.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ProductsApiCount200Response.


        :param count: The count of this ProductsApiCount200Response.
        :type count: int
        """

        self._count = count
