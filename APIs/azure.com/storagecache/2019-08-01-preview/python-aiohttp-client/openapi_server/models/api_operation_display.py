# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ApiOperationDisplay(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, operation: str=None, provider: str=None, resource: str=None):
        """ApiOperationDisplay - a model defined in OpenAPI

        :param operation: The operation of this ApiOperationDisplay.
        :param provider: The provider of this ApiOperationDisplay.
        :param resource: The resource of this ApiOperationDisplay.
        """
        self.openapi_types = {
            'operation': str,
            'provider': str,
            'resource': str
        }

        self.attribute_map = {
            'operation': 'operation',
            'provider': 'provider',
            'resource': 'resource'
        }

        self._operation = operation
        self._provider = provider
        self._resource = resource

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiOperationDisplay':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ApiOperation_display of this ApiOperationDisplay.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def operation(self):
        """Gets the operation of this ApiOperationDisplay.

        Operation type: Read, write, delete, etc.

        :return: The operation of this ApiOperationDisplay.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this ApiOperationDisplay.

        Operation type: Read, write, delete, etc.

        :param operation: The operation of this ApiOperationDisplay.
        :type operation: str
        """

        self._operation = operation

    @property
    def provider(self):
        """Gets the provider of this ApiOperationDisplay.

        Service provider: Microsoft.StorageCache

        :return: The provider of this ApiOperationDisplay.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ApiOperationDisplay.

        Service provider: Microsoft.StorageCache

        :param provider: The provider of this ApiOperationDisplay.
        :type provider: str
        """

        self._provider = provider

    @property
    def resource(self):
        """Gets the resource of this ApiOperationDisplay.

        Resource on which the operation is performed: cache, etc.

        :return: The resource of this ApiOperationDisplay.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ApiOperationDisplay.

        Resource on which the operation is performed: cache, etc.

        :param resource: The resource of this ApiOperationDisplay.
        :type resource: str
        """

        self._resource = resource
