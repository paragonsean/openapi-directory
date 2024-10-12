# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.data_lake_store_account_properties import DataLakeStoreAccountProperties
from openapi_server.models.encryption_identity import EncryptionIdentity
from openapi_server import util


class DataLakeStoreAccount(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, identity: EncryptionIdentity=None, properties: DataLakeStoreAccountProperties=None, id: str=None, location: str=None, name: str=None, tags: Dict[str, str]=None, type: str=None):
        """DataLakeStoreAccount - a model defined in OpenAPI

        :param identity: The identity of this DataLakeStoreAccount.
        :param properties: The properties of this DataLakeStoreAccount.
        :param id: The id of this DataLakeStoreAccount.
        :param location: The location of this DataLakeStoreAccount.
        :param name: The name of this DataLakeStoreAccount.
        :param tags: The tags of this DataLakeStoreAccount.
        :param type: The type of this DataLakeStoreAccount.
        """
        self.openapi_types = {
            'identity': EncryptionIdentity,
            'properties': DataLakeStoreAccountProperties,
            'id': str,
            'location': str,
            'name': str,
            'tags': Dict[str, str],
            'type': str
        }

        self.attribute_map = {
            'identity': 'identity',
            'properties': 'properties',
            'id': 'id',
            'location': 'location',
            'name': 'name',
            'tags': 'tags',
            'type': 'type'
        }

        self._identity = identity
        self._properties = properties
        self._id = id
        self._location = location
        self._name = name
        self._tags = tags
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DataLakeStoreAccount':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DataLakeStoreAccount of this DataLakeStoreAccount.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def identity(self):
        """Gets the identity of this DataLakeStoreAccount.


        :return: The identity of this DataLakeStoreAccount.
        :rtype: EncryptionIdentity
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this DataLakeStoreAccount.


        :param identity: The identity of this DataLakeStoreAccount.
        :type identity: EncryptionIdentity
        """

        self._identity = identity

    @property
    def properties(self):
        """Gets the properties of this DataLakeStoreAccount.


        :return: The properties of this DataLakeStoreAccount.
        :rtype: DataLakeStoreAccountProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DataLakeStoreAccount.


        :param properties: The properties of this DataLakeStoreAccount.
        :type properties: DataLakeStoreAccountProperties
        """

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this DataLakeStoreAccount.

        The resource identifier.

        :return: The id of this DataLakeStoreAccount.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataLakeStoreAccount.

        The resource identifier.

        :param id: The id of this DataLakeStoreAccount.
        :type id: str
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this DataLakeStoreAccount.

        The resource location.

        :return: The location of this DataLakeStoreAccount.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DataLakeStoreAccount.

        The resource location.

        :param location: The location of this DataLakeStoreAccount.
        :type location: str
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this DataLakeStoreAccount.

        The resource name.

        :return: The name of this DataLakeStoreAccount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataLakeStoreAccount.

        The resource name.

        :param name: The name of this DataLakeStoreAccount.
        :type name: str
        """

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this DataLakeStoreAccount.

        The resource tags.

        :return: The tags of this DataLakeStoreAccount.
        :rtype: Dict[str, str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DataLakeStoreAccount.

        The resource tags.

        :param tags: The tags of this DataLakeStoreAccount.
        :type tags: Dict[str, str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this DataLakeStoreAccount.

        The resource type.

        :return: The type of this DataLakeStoreAccount.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DataLakeStoreAccount.

        The resource type.

        :param type: The type of this DataLakeStoreAccount.
        :type type: str
        """

        self._type = type
