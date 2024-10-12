# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.brand_family import BrandFamily
from openapi_server import util


class Brand(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, brand_family: BrandFamily=None, key: str=None, logo_large_url: str=None, logo_url: str=None, name: str=None, shop_url: str=None):
        """Brand - a model defined in OpenAPI

        :param brand_family: The brand_family of this Brand.
        :param key: The key of this Brand.
        :param logo_large_url: The logo_large_url of this Brand.
        :param logo_url: The logo_url of this Brand.
        :param name: The name of this Brand.
        :param shop_url: The shop_url of this Brand.
        """
        self.openapi_types = {
            'brand_family': BrandFamily,
            'key': str,
            'logo_large_url': str,
            'logo_url': str,
            'name': str,
            'shop_url': str
        }

        self.attribute_map = {
            'brand_family': 'brandFamily',
            'key': 'key',
            'logo_large_url': 'logoLargeUrl',
            'logo_url': 'logoUrl',
            'name': 'name',
            'shop_url': 'shopUrl'
        }

        self._brand_family = brand_family
        self._key = key
        self._logo_large_url = logo_large_url
        self._logo_url = logo_url
        self._name = name
        self._shop_url = shop_url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Brand':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Brand of this Brand.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def brand_family(self):
        """Gets the brand_family of this Brand.


        :return: The brand_family of this Brand.
        :rtype: BrandFamily
        """
        return self._brand_family

    @brand_family.setter
    def brand_family(self, brand_family):
        """Sets the brand_family of this Brand.


        :param brand_family: The brand_family of this Brand.
        :type brand_family: BrandFamily
        """

        self._brand_family = brand_family

    @property
    def key(self):
        """Gets the key of this Brand.

        The unique key for a brand

        :return: The key of this Brand.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Brand.

        The unique key for a brand

        :param key: The key of this Brand.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def logo_large_url(self):
        """Gets the logo_large_url of this Brand.

        The url of the large brand logo within the Zalando web shop

        :return: The logo_large_url of this Brand.
        :rtype: str
        """
        return self._logo_large_url

    @logo_large_url.setter
    def logo_large_url(self, logo_large_url):
        """Sets the logo_large_url of this Brand.

        The url of the large brand logo within the Zalando web shop

        :param logo_large_url: The logo_large_url of this Brand.
        :type logo_large_url: str
        """

        self._logo_large_url = logo_large_url

    @property
    def logo_url(self):
        """Gets the logo_url of this Brand.

        The url of the brand logo within the Zalando web shop

        :return: The logo_url of this Brand.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this Brand.

        The url of the brand logo within the Zalando web shop

        :param logo_url: The logo_url of this Brand.
        :type logo_url: str
        """

        self._logo_url = logo_url

    @property
    def name(self):
        """Gets the name of this Brand.

        Name of the brand

        :return: The name of this Brand.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Brand.

        Name of the brand

        :param name: The name of this Brand.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def shop_url(self):
        """Gets the shop_url of this Brand.

        The url of the brand within the Zalando web shop

        :return: The shop_url of this Brand.
        :rtype: str
        """
        return self._shop_url

    @shop_url.setter
    def shop_url(self, shop_url):
        """Sets the shop_url of this Brand.

        The url of the brand within the Zalando web shop

        :param shop_url: The shop_url of this Brand.
        :type shop_url: str
        """
        if shop_url is None:
            raise ValueError("Invalid value for `shop_url`, must not be `None`")

        self._shop_url = shop_url
