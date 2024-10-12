# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CatalogDataProductRenderFormattedPriceInfoInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, extension_attributes: object=None, final_price: str=None, max_price: str=None, max_regular_price: str=None, minimal_price: str=None, minimal_regular_price: str=None, regular_price: str=None, special_price: str=None):
        """CatalogDataProductRenderFormattedPriceInfoInterface - a model defined in OpenAPI

        :param extension_attributes: The extension_attributes of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :param final_price: The final_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :param max_price: The max_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :param max_regular_price: The max_regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :param minimal_price: The minimal_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :param minimal_regular_price: The minimal_regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :param regular_price: The regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :param special_price: The special_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        """
        self.openapi_types = {
            'extension_attributes': object,
            'final_price': str,
            'max_price': str,
            'max_regular_price': str,
            'minimal_price': str,
            'minimal_regular_price': str,
            'regular_price': str,
            'special_price': str
        }

        self.attribute_map = {
            'extension_attributes': 'extension_attributes',
            'final_price': 'final_price',
            'max_price': 'max_price',
            'max_regular_price': 'max_regular_price',
            'minimal_price': 'minimal_price',
            'minimal_regular_price': 'minimal_regular_price',
            'regular_price': 'regular_price',
            'special_price': 'special_price'
        }

        self._extension_attributes = extension_attributes
        self._final_price = final_price
        self._max_price = max_price
        self._max_regular_price = max_regular_price
        self._minimal_price = minimal_price
        self._minimal_regular_price = minimal_regular_price
        self._regular_price = regular_price
        self._special_price = special_price

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CatalogDataProductRenderFormattedPriceInfoInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The catalog-data-product-render-formatted-price-info-interface of this CatalogDataProductRenderFormattedPriceInfoInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this CatalogDataProductRenderFormattedPriceInfoInterface.

        ExtensionInterface class for @see \\Magento\\Catalog\\Api\\Data\\ProductRender\\FormattedPriceInfoInterface

        :return: The extension_attributes of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this CatalogDataProductRenderFormattedPriceInfoInterface.

        ExtensionInterface class for @see \\Magento\\Catalog\\Api\\Data\\ProductRender\\FormattedPriceInfoInterface

        :param extension_attributes: The extension_attributes of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes

    @property
    def final_price(self):
        """Gets the final_price of this CatalogDataProductRenderFormattedPriceInfoInterface.

        Html with final price

        :return: The final_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :rtype: str
        """
        return self._final_price

    @final_price.setter
    def final_price(self, final_price):
        """Sets the final_price of this CatalogDataProductRenderFormattedPriceInfoInterface.

        Html with final price

        :param final_price: The final_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :type final_price: str
        """
        if final_price is None:
            raise ValueError("Invalid value for `final_price`, must not be `None`")

        self._final_price = final_price

    @property
    def max_price(self):
        """Gets the max_price of this CatalogDataProductRenderFormattedPriceInfoInterface.

        Max price of a product

        :return: The max_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :rtype: str
        """
        return self._max_price

    @max_price.setter
    def max_price(self, max_price):
        """Sets the max_price of this CatalogDataProductRenderFormattedPriceInfoInterface.

        Max price of a product

        :param max_price: The max_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :type max_price: str
        """
        if max_price is None:
            raise ValueError("Invalid value for `max_price`, must not be `None`")

        self._max_price = max_price

    @property
    def max_regular_price(self):
        """Gets the max_regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.

        Max regular price

        :return: The max_regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :rtype: str
        """
        return self._max_regular_price

    @max_regular_price.setter
    def max_regular_price(self, max_regular_price):
        """Sets the max_regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.

        Max regular price

        :param max_regular_price: The max_regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :type max_regular_price: str
        """
        if max_regular_price is None:
            raise ValueError("Invalid value for `max_regular_price`, must not be `None`")

        self._max_regular_price = max_regular_price

    @property
    def minimal_price(self):
        """Gets the minimal_price of this CatalogDataProductRenderFormattedPriceInfoInterface.

        The minimal price of the product or variation

        :return: The minimal_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :rtype: str
        """
        return self._minimal_price

    @minimal_price.setter
    def minimal_price(self, minimal_price):
        """Sets the minimal_price of this CatalogDataProductRenderFormattedPriceInfoInterface.

        The minimal price of the product or variation

        :param minimal_price: The minimal_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :type minimal_price: str
        """
        if minimal_price is None:
            raise ValueError("Invalid value for `minimal_price`, must not be `None`")

        self._minimal_price = minimal_price

    @property
    def minimal_regular_price(self):
        """Gets the minimal_regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.

        Minimal regular price

        :return: The minimal_regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :rtype: str
        """
        return self._minimal_regular_price

    @minimal_regular_price.setter
    def minimal_regular_price(self, minimal_regular_price):
        """Sets the minimal_regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.

        Minimal regular price

        :param minimal_regular_price: The minimal_regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :type minimal_regular_price: str
        """
        if minimal_regular_price is None:
            raise ValueError("Invalid value for `minimal_regular_price`, must not be `None`")

        self._minimal_regular_price = minimal_regular_price

    @property
    def regular_price(self):
        """Gets the regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.

        Price - is price of product without discounts and special price with taxes and fixed product tax

        :return: The regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :rtype: str
        """
        return self._regular_price

    @regular_price.setter
    def regular_price(self, regular_price):
        """Sets the regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.

        Price - is price of product without discounts and special price with taxes and fixed product tax

        :param regular_price: The regular_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :type regular_price: str
        """
        if regular_price is None:
            raise ValueError("Invalid value for `regular_price`, must not be `None`")

        self._regular_price = regular_price

    @property
    def special_price(self):
        """Gets the special_price of this CatalogDataProductRenderFormattedPriceInfoInterface.

        Special price

        :return: The special_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :rtype: str
        """
        return self._special_price

    @special_price.setter
    def special_price(self, special_price):
        """Sets the special_price of this CatalogDataProductRenderFormattedPriceInfoInterface.

        Special price

        :param special_price: The special_price of this CatalogDataProductRenderFormattedPriceInfoInterface.
        :type special_price: str
        """
        if special_price is None:
            raise ValueError("Invalid value for `special_price`, must not be `None`")

        self._special_price = special_price
