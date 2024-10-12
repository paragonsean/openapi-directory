# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.import_extension_properties import ImportExtensionProperties
from openapi_server import util


class ImportExtensionRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, properties: ImportExtensionProperties=None, type: str=None):
        """ImportExtensionRequest - a model defined in OpenAPI

        :param name: The name of this ImportExtensionRequest.
        :param properties: The properties of this ImportExtensionRequest.
        :param type: The type of this ImportExtensionRequest.
        """
        self.openapi_types = {
            'name': str,
            'properties': ImportExtensionProperties,
            'type': str
        }

        self.attribute_map = {
            'name': 'name',
            'properties': 'properties',
            'type': 'type'
        }

        self._name = name
        self._properties = properties
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ImportExtensionRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ImportExtensionRequest of this ImportExtensionRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ImportExtensionRequest.

        The name of the extension.

        :return: The name of this ImportExtensionRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportExtensionRequest.

        The name of the extension.

        :param name: The name of this ImportExtensionRequest.
        :type name: str
        """

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this ImportExtensionRequest.


        :return: The properties of this ImportExtensionRequest.
        :rtype: ImportExtensionProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ImportExtensionRequest.


        :param properties: The properties of this ImportExtensionRequest.
        :type properties: ImportExtensionProperties
        """

        self._properties = properties

    @property
    def type(self):
        """Gets the type of this ImportExtensionRequest.

        The type of the extension.

        :return: The type of this ImportExtensionRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImportExtensionRequest.

        The type of the extension.

        :param type: The type of this ImportExtensionRequest.
        :type type: str
        """

        self._type = type
