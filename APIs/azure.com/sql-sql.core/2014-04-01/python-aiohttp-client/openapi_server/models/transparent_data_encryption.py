# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.transparent_data_encryption_properties import TransparentDataEncryptionProperties
from openapi_server import util


class TransparentDataEncryption(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, location: str=None, properties: TransparentDataEncryptionProperties=None, id: str=None, name: str=None, type: str=None):
        """TransparentDataEncryption - a model defined in OpenAPI

        :param location: The location of this TransparentDataEncryption.
        :param properties: The properties of this TransparentDataEncryption.
        :param id: The id of this TransparentDataEncryption.
        :param name: The name of this TransparentDataEncryption.
        :param type: The type of this TransparentDataEncryption.
        """
        self.openapi_types = {
            'location': str,
            'properties': TransparentDataEncryptionProperties,
            'id': str,
            'name': str,
            'type': str
        }

        self.attribute_map = {
            'location': 'location',
            'properties': 'properties',
            'id': 'id',
            'name': 'name',
            'type': 'type'
        }

        self._location = location
        self._properties = properties
        self._id = id
        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TransparentDataEncryption':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TransparentDataEncryption of this TransparentDataEncryption.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def location(self):
        """Gets the location of this TransparentDataEncryption.

        Resource location.

        :return: The location of this TransparentDataEncryption.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this TransparentDataEncryption.

        Resource location.

        :param location: The location of this TransparentDataEncryption.
        :type location: str
        """

        self._location = location

    @property
    def properties(self):
        """Gets the properties of this TransparentDataEncryption.


        :return: The properties of this TransparentDataEncryption.
        :rtype: TransparentDataEncryptionProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TransparentDataEncryption.


        :param properties: The properties of this TransparentDataEncryption.
        :type properties: TransparentDataEncryptionProperties
        """

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this TransparentDataEncryption.

        Resource ID.

        :return: The id of this TransparentDataEncryption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransparentDataEncryption.

        Resource ID.

        :param id: The id of this TransparentDataEncryption.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TransparentDataEncryption.

        Resource name.

        :return: The name of this TransparentDataEncryption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TransparentDataEncryption.

        Resource name.

        :param name: The name of this TransparentDataEncryption.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this TransparentDataEncryption.

        Resource type.

        :return: The type of this TransparentDataEncryption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransparentDataEncryption.

        Resource type.

        :param type: The type of this TransparentDataEncryption.
        :type type: str
        """

        self._type = type
