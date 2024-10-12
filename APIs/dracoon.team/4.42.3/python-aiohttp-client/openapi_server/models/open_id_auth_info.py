# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.open_id_provider import OpenIdProvider
from openapi_server import util


class OpenIdAuthInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, items: List[OpenIdProvider]=None):
        """OpenIdAuthInfo - a model defined in OpenAPI

        :param items: The items of this OpenIdAuthInfo.
        """
        self.openapi_types = {
            'items': List[OpenIdProvider]
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = items

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OpenIdAuthInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OpenIdAuthInfo of this OpenIdAuthInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self):
        """Gets the items of this OpenIdAuthInfo.

        List of available OpenID Connect identity providers

        :return: The items of this OpenIdAuthInfo.
        :rtype: List[OpenIdProvider]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this OpenIdAuthInfo.

        List of available OpenID Connect identity providers

        :param items: The items of this OpenIdAuthInfo.
        :type items: List[OpenIdProvider]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items
