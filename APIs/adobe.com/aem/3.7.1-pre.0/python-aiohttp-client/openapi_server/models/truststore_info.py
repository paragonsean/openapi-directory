# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.truststore_items import TruststoreItems
from openapi_server import util


class TruststoreInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, aliases: List[TruststoreItems]=None, exists: bool=None):
        """TruststoreInfo - a model defined in OpenAPI

        :param aliases: The aliases of this TruststoreInfo.
        :param exists: The exists of this TruststoreInfo.
        """
        self.openapi_types = {
            'aliases': List[TruststoreItems],
            'exists': bool
        }

        self.attribute_map = {
            'aliases': 'aliases',
            'exists': 'exists'
        }

        self._aliases = aliases
        self._exists = exists

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TruststoreInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TruststoreInfo of this TruststoreInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def aliases(self):
        """Gets the aliases of this TruststoreInfo.


        :return: The aliases of this TruststoreInfo.
        :rtype: List[TruststoreItems]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this TruststoreInfo.


        :param aliases: The aliases of this TruststoreInfo.
        :type aliases: List[TruststoreItems]
        """

        self._aliases = aliases

    @property
    def exists(self):
        """Gets the exists of this TruststoreInfo.

        False if truststore don't exist

        :return: The exists of this TruststoreInfo.
        :rtype: bool
        """
        return self._exists

    @exists.setter
    def exists(self, exists):
        """Sets the exists of this TruststoreInfo.

        False if truststore don't exist

        :param exists: The exists of this TruststoreInfo.
        :type exists: bool
        """

        self._exists = exists
