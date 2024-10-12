# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.product_model import ProductModel
from openapi_server import util


class EnvironmentModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, color: str=None, description: str=None, environment_id: str=None, name: str=None, order: int=None, product: ProductModel=None, reason_required: bool=None):
        """EnvironmentModel - a model defined in OpenAPI

        :param color: The color of this EnvironmentModel.
        :param description: The description of this EnvironmentModel.
        :param environment_id: The environment_id of this EnvironmentModel.
        :param name: The name of this EnvironmentModel.
        :param order: The order of this EnvironmentModel.
        :param product: The product of this EnvironmentModel.
        :param reason_required: The reason_required of this EnvironmentModel.
        """
        self.openapi_types = {
            'color': str,
            'description': str,
            'environment_id': str,
            'name': str,
            'order': int,
            'product': ProductModel,
            'reason_required': bool
        }

        self.attribute_map = {
            'color': 'color',
            'description': 'description',
            'environment_id': 'environmentId',
            'name': 'name',
            'order': 'order',
            'product': 'product',
            'reason_required': 'reasonRequired'
        }

        self._color = color
        self._description = description
        self._environment_id = environment_id
        self._name = name
        self._order = order
        self._product = product
        self._reason_required = reason_required

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EnvironmentModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EnvironmentModel of this EnvironmentModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def color(self):
        """Gets the color of this EnvironmentModel.


        :return: The color of this EnvironmentModel.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this EnvironmentModel.


        :param color: The color of this EnvironmentModel.
        :type color: str
        """

        self._color = color

    @property
    def description(self):
        """Gets the description of this EnvironmentModel.


        :return: The description of this EnvironmentModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EnvironmentModel.


        :param description: The description of this EnvironmentModel.
        :type description: str
        """

        self._description = description

    @property
    def environment_id(self):
        """Gets the environment_id of this EnvironmentModel.


        :return: The environment_id of this EnvironmentModel.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this EnvironmentModel.


        :param environment_id: The environment_id of this EnvironmentModel.
        :type environment_id: str
        """

        self._environment_id = environment_id

    @property
    def name(self):
        """Gets the name of this EnvironmentModel.


        :return: The name of this EnvironmentModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvironmentModel.


        :param name: The name of this EnvironmentModel.
        :type name: str
        """

        self._name = name

    @property
    def order(self):
        """Gets the order of this EnvironmentModel.


        :return: The order of this EnvironmentModel.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this EnvironmentModel.


        :param order: The order of this EnvironmentModel.
        :type order: int
        """

        self._order = order

    @property
    def product(self):
        """Gets the product of this EnvironmentModel.


        :return: The product of this EnvironmentModel.
        :rtype: ProductModel
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this EnvironmentModel.


        :param product: The product of this EnvironmentModel.
        :type product: ProductModel
        """

        self._product = product

    @property
    def reason_required(self):
        """Gets the reason_required of this EnvironmentModel.


        :return: The reason_required of this EnvironmentModel.
        :rtype: bool
        """
        return self._reason_required

    @reason_required.setter
    def reason_required(self, reason_required):
        """Sets the reason_required of this EnvironmentModel.


        :param reason_required: The reason_required of this EnvironmentModel.
        :type reason_required: bool
        """

        self._reason_required = reason_required
