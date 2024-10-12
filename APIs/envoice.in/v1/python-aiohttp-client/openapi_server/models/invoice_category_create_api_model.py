# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InvoiceCategoryCreateApiModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None):
        """InvoiceCategoryCreateApiModel - a model defined in OpenAPI

        :param name: The name of this InvoiceCategoryCreateApiModel.
        """
        self.openapi_types = {
            'name': str
        }

        self.attribute_map = {
            'name': 'Name'
        }

        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InvoiceCategoryCreateApiModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The InvoiceCategoryCreateApiModel of this InvoiceCategoryCreateApiModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this InvoiceCategoryCreateApiModel.

        Category name

        :return: The name of this InvoiceCategoryCreateApiModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InvoiceCategoryCreateApiModel.

        Category name

        :param name: The name of this InvoiceCategoryCreateApiModel.
        :type name: str
        """

        self._name = name
