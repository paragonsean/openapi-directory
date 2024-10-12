# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.quote_data_cart_item_extension_interface import QuoteDataCartItemExtensionInterface
from openapi_server.models.quote_data_product_option_interface import QuoteDataProductOptionInterface
from openapi_server import util


class QuoteDataCartItemInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, extension_attributes: QuoteDataCartItemExtensionInterface=None, item_id: int=None, name: str=None, price: float=None, product_option: QuoteDataProductOptionInterface=None, product_type: str=None, qty: float=None, quote_id: str=None, sku: str=None):
        """QuoteDataCartItemInterface - a model defined in OpenAPI

        :param extension_attributes: The extension_attributes of this QuoteDataCartItemInterface.
        :param item_id: The item_id of this QuoteDataCartItemInterface.
        :param name: The name of this QuoteDataCartItemInterface.
        :param price: The price of this QuoteDataCartItemInterface.
        :param product_option: The product_option of this QuoteDataCartItemInterface.
        :param product_type: The product_type of this QuoteDataCartItemInterface.
        :param qty: The qty of this QuoteDataCartItemInterface.
        :param quote_id: The quote_id of this QuoteDataCartItemInterface.
        :param sku: The sku of this QuoteDataCartItemInterface.
        """
        self.openapi_types = {
            'extension_attributes': QuoteDataCartItemExtensionInterface,
            'item_id': int,
            'name': str,
            'price': float,
            'product_option': QuoteDataProductOptionInterface,
            'product_type': str,
            'qty': float,
            'quote_id': str,
            'sku': str
        }

        self.attribute_map = {
            'extension_attributes': 'extension_attributes',
            'item_id': 'item_id',
            'name': 'name',
            'price': 'price',
            'product_option': 'product_option',
            'product_type': 'product_type',
            'qty': 'qty',
            'quote_id': 'quote_id',
            'sku': 'sku'
        }

        self._extension_attributes = extension_attributes
        self._item_id = item_id
        self._name = name
        self._price = price
        self._product_option = product_option
        self._product_type = product_type
        self._qty = qty
        self._quote_id = quote_id
        self._sku = sku

    @classmethod
    def from_dict(cls, dikt: dict) -> 'QuoteDataCartItemInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The quote-data-cart-item-interface of this QuoteDataCartItemInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this QuoteDataCartItemInterface.


        :return: The extension_attributes of this QuoteDataCartItemInterface.
        :rtype: QuoteDataCartItemExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this QuoteDataCartItemInterface.


        :param extension_attributes: The extension_attributes of this QuoteDataCartItemInterface.
        :type extension_attributes: QuoteDataCartItemExtensionInterface
        """

        self._extension_attributes = extension_attributes

    @property
    def item_id(self):
        """Gets the item_id of this QuoteDataCartItemInterface.

        Item ID. Otherwise, null.

        :return: The item_id of this QuoteDataCartItemInterface.
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this QuoteDataCartItemInterface.

        Item ID. Otherwise, null.

        :param item_id: The item_id of this QuoteDataCartItemInterface.
        :type item_id: int
        """

        self._item_id = item_id

    @property
    def name(self):
        """Gets the name of this QuoteDataCartItemInterface.

        Product name. Otherwise, null.

        :return: The name of this QuoteDataCartItemInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QuoteDataCartItemInterface.

        Product name. Otherwise, null.

        :param name: The name of this QuoteDataCartItemInterface.
        :type name: str
        """

        self._name = name

    @property
    def price(self):
        """Gets the price of this QuoteDataCartItemInterface.

        Product price. Otherwise, null.

        :return: The price of this QuoteDataCartItemInterface.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this QuoteDataCartItemInterface.

        Product price. Otherwise, null.

        :param price: The price of this QuoteDataCartItemInterface.
        :type price: float
        """

        self._price = price

    @property
    def product_option(self):
        """Gets the product_option of this QuoteDataCartItemInterface.


        :return: The product_option of this QuoteDataCartItemInterface.
        :rtype: QuoteDataProductOptionInterface
        """
        return self._product_option

    @product_option.setter
    def product_option(self, product_option):
        """Sets the product_option of this QuoteDataCartItemInterface.


        :param product_option: The product_option of this QuoteDataCartItemInterface.
        :type product_option: QuoteDataProductOptionInterface
        """

        self._product_option = product_option

    @property
    def product_type(self):
        """Gets the product_type of this QuoteDataCartItemInterface.

        Product type. Otherwise, null.

        :return: The product_type of this QuoteDataCartItemInterface.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this QuoteDataCartItemInterface.

        Product type. Otherwise, null.

        :param product_type: The product_type of this QuoteDataCartItemInterface.
        :type product_type: str
        """

        self._product_type = product_type

    @property
    def qty(self):
        """Gets the qty of this QuoteDataCartItemInterface.

        Product quantity.

        :return: The qty of this QuoteDataCartItemInterface.
        :rtype: float
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this QuoteDataCartItemInterface.

        Product quantity.

        :param qty: The qty of this QuoteDataCartItemInterface.
        :type qty: float
        """
        if qty is None:
            raise ValueError("Invalid value for `qty`, must not be `None`")

        self._qty = qty

    @property
    def quote_id(self):
        """Gets the quote_id of this QuoteDataCartItemInterface.

        Quote id.

        :return: The quote_id of this QuoteDataCartItemInterface.
        :rtype: str
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this QuoteDataCartItemInterface.

        Quote id.

        :param quote_id: The quote_id of this QuoteDataCartItemInterface.
        :type quote_id: str
        """
        if quote_id is None:
            raise ValueError("Invalid value for `quote_id`, must not be `None`")

        self._quote_id = quote_id

    @property
    def sku(self):
        """Gets the sku of this QuoteDataCartItemInterface.

        Product SKU. Otherwise, null.

        :return: The sku of this QuoteDataCartItemInterface.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this QuoteDataCartItemInterface.

        Product SKU. Otherwise, null.

        :param sku: The sku of this QuoteDataCartItemInterface.
        :type sku: str
        """

        self._sku = sku
