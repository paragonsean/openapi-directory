# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.universal_do_not_contact import UniversalDoNotContact
from openapi_server import util


class ItemListUniversalDoNotContact(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, items: List[UniversalDoNotContact]=None):
        """ItemListUniversalDoNotContact - a model defined in OpenAPI

        :param items: The items of this ItemListUniversalDoNotContact.
        """
        self.openapi_types = {
            'items': List[UniversalDoNotContact]
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = items

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ItemListUniversalDoNotContact':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ItemListUniversalDoNotContact of this ItemListUniversalDoNotContact.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self):
        """Gets the items of this ItemListUniversalDoNotContact.

        ~

        :return: The items of this ItemListUniversalDoNotContact.
        :rtype: List[UniversalDoNotContact]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ItemListUniversalDoNotContact.

        ~

        :param items: The items of this ItemListUniversalDoNotContact.
        :type items: List[UniversalDoNotContact]
        """

        self._items = items
