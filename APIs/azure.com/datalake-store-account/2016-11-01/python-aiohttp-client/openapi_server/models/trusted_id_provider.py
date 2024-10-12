# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.trusted_id_provider_properties import TrustedIdProviderProperties
from openapi_server import util


class TrustedIdProvider(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, properties: TrustedIdProviderProperties=None, id: str=None, name: str=None, type: str=None):
        """TrustedIdProvider - a model defined in OpenAPI

        :param properties: The properties of this TrustedIdProvider.
        :param id: The id of this TrustedIdProvider.
        :param name: The name of this TrustedIdProvider.
        :param type: The type of this TrustedIdProvider.
        """
        self.openapi_types = {
            'properties': TrustedIdProviderProperties,
            'id': str,
            'name': str,
            'type': str
        }

        self.attribute_map = {
            'properties': 'properties',
            'id': 'id',
            'name': 'name',
            'type': 'type'
        }

        self._properties = properties
        self._id = id
        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TrustedIdProvider':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TrustedIdProvider of this TrustedIdProvider.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def properties(self):
        """Gets the properties of this TrustedIdProvider.


        :return: The properties of this TrustedIdProvider.
        :rtype: TrustedIdProviderProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TrustedIdProvider.


        :param properties: The properties of this TrustedIdProvider.
        :type properties: TrustedIdProviderProperties
        """

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this TrustedIdProvider.

        The resource identifier.

        :return: The id of this TrustedIdProvider.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrustedIdProvider.

        The resource identifier.

        :param id: The id of this TrustedIdProvider.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TrustedIdProvider.

        The resource name.

        :return: The name of this TrustedIdProvider.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrustedIdProvider.

        The resource name.

        :param name: The name of this TrustedIdProvider.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this TrustedIdProvider.

        The resource type.

        :return: The type of this TrustedIdProvider.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TrustedIdProvider.

        The resource type.

        :param type: The type of this TrustedIdProvider.
        :type type: str
        """

        self._type = type
