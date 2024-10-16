# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SigningConfig(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, has_store_file: bool=None):
        """SigningConfig - a model defined in OpenAPI

        :param has_store_file: The has_store_file of this SigningConfig.
        """
        self.openapi_types = {
            'has_store_file': bool
        }

        self.attribute_map = {
            'has_store_file': 'hasStoreFile'
        }

        self._has_store_file = has_store_file

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SigningConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SigningConfig of this SigningConfig.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_store_file(self):
        """Gets the has_store_file of this SigningConfig.

        Indicates if storeFile is specified in the signing configuration

        :return: The has_store_file of this SigningConfig.
        :rtype: bool
        """
        return self._has_store_file

    @has_store_file.setter
    def has_store_file(self, has_store_file):
        """Sets the has_store_file of this SigningConfig.

        Indicates if storeFile is specified in the signing configuration

        :param has_store_file: The has_store_file of this SigningConfig.
        :type has_store_file: bool
        """

        self._has_store_file = has_store_file
