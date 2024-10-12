# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.product_tax_add_tax_rates_inner import ProductTaxAddTaxRatesInner
from openapi_server import util


class ProductTaxAdd(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, product_id: str=None, tax_rates: List[ProductTaxAddTaxRatesInner]=None):
        """ProductTaxAdd - a model defined in OpenAPI

        :param name: The name of this ProductTaxAdd.
        :param product_id: The product_id of this ProductTaxAdd.
        :param tax_rates: The tax_rates of this ProductTaxAdd.
        """
        self.openapi_types = {
            'name': str,
            'product_id': str,
            'tax_rates': List[ProductTaxAddTaxRatesInner]
        }

        self.attribute_map = {
            'name': 'name',
            'product_id': 'product_id',
            'tax_rates': 'tax_rates'
        }

        self._name = name
        self._product_id = product_id
        self._tax_rates = tax_rates

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProductTaxAdd':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProductTaxAdd of this ProductTaxAdd.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ProductTaxAdd.

        Defines tax class name where tax has to be added

        :return: The name of this ProductTaxAdd.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductTaxAdd.

        Defines tax class name where tax has to be added

        :param name: The name of this ProductTaxAdd.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def product_id(self):
        """Gets the product_id of this ProductTaxAdd.

        Defines products specified by product id

        :return: The product_id of this ProductTaxAdd.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductTaxAdd.

        Defines products specified by product id

        :param product_id: The product_id of this ProductTaxAdd.
        :type product_id: str
        """

        self._product_id = product_id

    @property
    def tax_rates(self):
        """Gets the tax_rates of this ProductTaxAdd.

        Defines tax rates of specified tax classes

        :return: The tax_rates of this ProductTaxAdd.
        :rtype: List[ProductTaxAddTaxRatesInner]
        """
        return self._tax_rates

    @tax_rates.setter
    def tax_rates(self, tax_rates):
        """Sets the tax_rates of this ProductTaxAdd.

        Defines tax rates of specified tax classes

        :param tax_rates: The tax_rates of this ProductTaxAdd.
        :type tax_rates: List[ProductTaxAddTaxRatesInner]
        """
        if tax_rates is None:
            raise ValueError("Invalid value for `tax_rates`, must not be `None`")

        self._tax_rates = tax_rates
