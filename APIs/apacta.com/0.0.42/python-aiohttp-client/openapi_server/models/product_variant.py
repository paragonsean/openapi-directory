# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ProductVariant(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, price: float=None, product_number: str=None, variant_id: str=None, variant_type: str=None):
        """ProductVariant - a model defined in OpenAPI

        :param name: The name of this ProductVariant.
        :param price: The price of this ProductVariant.
        :param product_number: The product_number of this ProductVariant.
        :param variant_id: The variant_id of this ProductVariant.
        :param variant_type: The variant_type of this ProductVariant.
        """
        self.openapi_types = {
            'name': str,
            'price': float,
            'product_number': str,
            'variant_id': str,
            'variant_type': str
        }

        self.attribute_map = {
            'name': 'name',
            'price': 'price',
            'product_number': 'product_number',
            'variant_id': 'variant_id',
            'variant_type': 'variant_type'
        }

        self._name = name
        self._price = price
        self._product_number = product_number
        self._variant_id = variant_id
        self._variant_type = variant_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProductVariant':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProductVariant of this ProductVariant.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ProductVariant.


        :return: The name of this ProductVariant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductVariant.


        :param name: The name of this ProductVariant.
        :type name: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")

        self._name = name

    @property
    def price(self):
        """Gets the price of this ProductVariant.


        :return: The price of this ProductVariant.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ProductVariant.


        :param price: The price of this ProductVariant.
        :type price: float
        """

        self._price = price

    @property
    def product_number(self):
        """Gets the product_number of this ProductVariant.


        :return: The product_number of this ProductVariant.
        :rtype: str
        """
        return self._product_number

    @product_number.setter
    def product_number(self, product_number):
        """Sets the product_number of this ProductVariant.


        :param product_number: The product_number of this ProductVariant.
        :type product_number: str
        """
        if product_number is not None and len(product_number) > 255:
            raise ValueError("Invalid value for `product_number`, length must be less than or equal to `255`")

        self._product_number = product_number

    @property
    def variant_id(self):
        """Gets the variant_id of this ProductVariant.


        :return: The variant_id of this ProductVariant.
        :rtype: str
        """
        return self._variant_id

    @variant_id.setter
    def variant_id(self, variant_id):
        """Sets the variant_id of this ProductVariant.


        :param variant_id: The variant_id of this ProductVariant.
        :type variant_id: str
        """

        self._variant_id = variant_id

    @property
    def variant_type(self):
        """Gets the variant_type of this ProductVariant.


        :return: The variant_type of this ProductVariant.
        :rtype: str
        """
        return self._variant_type

    @variant_type.setter
    def variant_type(self, variant_type):
        """Sets the variant_type of this ProductVariant.


        :param variant_type: The variant_type of this ProductVariant.
        :type variant_type: str
        """
        allowed_values = ["expense_line", "vendor_product"]  # noqa: E501
        if variant_type not in allowed_values:
            raise ValueError(
                "Invalid value for `variant_type` ({0}), must be one of {1}"
                .format(variant_type, allowed_values)
            )

        self._variant_type = variant_type
