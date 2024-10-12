# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.provider_operation import ProviderOperation
from openapi_server.models.resource_type import ResourceType
from openapi_server import util


class ProviderOperationsMetadata(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, display_name: str=None, id: str=None, name: str=None, operations: List[ProviderOperation]=None, resource_types: List[ResourceType]=None, type: str=None):
        """ProviderOperationsMetadata - a model defined in OpenAPI

        :param display_name: The display_name of this ProviderOperationsMetadata.
        :param id: The id of this ProviderOperationsMetadata.
        :param name: The name of this ProviderOperationsMetadata.
        :param operations: The operations of this ProviderOperationsMetadata.
        :param resource_types: The resource_types of this ProviderOperationsMetadata.
        :param type: The type of this ProviderOperationsMetadata.
        """
        self.openapi_types = {
            'display_name': str,
            'id': str,
            'name': str,
            'operations': List[ProviderOperation],
            'resource_types': List[ResourceType],
            'type': str
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'id': 'id',
            'name': 'name',
            'operations': 'operations',
            'resource_types': 'resourceTypes',
            'type': 'type'
        }

        self._display_name = display_name
        self._id = id
        self._name = name
        self._operations = operations
        self._resource_types = resource_types
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProviderOperationsMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProviderOperationsMetadata of this ProviderOperationsMetadata.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def display_name(self):
        """Gets the display_name of this ProviderOperationsMetadata.

        The provider display name.

        :return: The display_name of this ProviderOperationsMetadata.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ProviderOperationsMetadata.

        The provider display name.

        :param display_name: The display_name of this ProviderOperationsMetadata.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this ProviderOperationsMetadata.

        The provider id.

        :return: The id of this ProviderOperationsMetadata.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProviderOperationsMetadata.

        The provider id.

        :param id: The id of this ProviderOperationsMetadata.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProviderOperationsMetadata.

        The provider name.

        :return: The name of this ProviderOperationsMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProviderOperationsMetadata.

        The provider name.

        :param name: The name of this ProviderOperationsMetadata.
        :type name: str
        """

        self._name = name

    @property
    def operations(self):
        """Gets the operations of this ProviderOperationsMetadata.

        The provider operations.

        :return: The operations of this ProviderOperationsMetadata.
        :rtype: List[ProviderOperation]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this ProviderOperationsMetadata.

        The provider operations.

        :param operations: The operations of this ProviderOperationsMetadata.
        :type operations: List[ProviderOperation]
        """

        self._operations = operations

    @property
    def resource_types(self):
        """Gets the resource_types of this ProviderOperationsMetadata.

        The provider resource types

        :return: The resource_types of this ProviderOperationsMetadata.
        :rtype: List[ResourceType]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        """Sets the resource_types of this ProviderOperationsMetadata.

        The provider resource types

        :param resource_types: The resource_types of this ProviderOperationsMetadata.
        :type resource_types: List[ResourceType]
        """

        self._resource_types = resource_types

    @property
    def type(self):
        """Gets the type of this ProviderOperationsMetadata.

        The provider type.

        :return: The type of this ProviderOperationsMetadata.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProviderOperationsMetadata.

        The provider type.

        :param type: The type of this ProviderOperationsMetadata.
        :type type: str
        """

        self._type = type
