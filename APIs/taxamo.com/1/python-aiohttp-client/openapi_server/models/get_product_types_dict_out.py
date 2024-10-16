# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.product_type_schema import ProductTypeSchema
from openapi_server import util


class GetProductTypesDictOut(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dictionary: List[ProductTypeSchema]=None):
        """GetProductTypesDictOut - a model defined in OpenAPI

        :param dictionary: The dictionary of this GetProductTypesDictOut.
        """
        self.openapi_types = {
            'dictionary': List[ProductTypeSchema]
        }

        self.attribute_map = {
            'dictionary': 'dictionary'
        }

        self._dictionary = dictionary

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetProductTypesDictOut':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getProductTypesDictOut of this GetProductTypesDictOut.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dictionary(self):
        """Gets the dictionary of this GetProductTypesDictOut.

        Product type dictionary.

        :return: The dictionary of this GetProductTypesDictOut.
        :rtype: List[ProductTypeSchema]
        """
        return self._dictionary

    @dictionary.setter
    def dictionary(self, dictionary):
        """Sets the dictionary of this GetProductTypesDictOut.

        Product type dictionary.

        :param dictionary: The dictionary of this GetProductTypesDictOut.
        :type dictionary: List[ProductTypeSchema]
        """

        self._dictionary = dictionary
