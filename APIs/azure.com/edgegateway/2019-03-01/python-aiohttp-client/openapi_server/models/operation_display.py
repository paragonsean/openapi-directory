# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OperationDisplay(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, operation: str=None, provider: str=None, resource: str=None):
        """OperationDisplay - a model defined in OpenAPI

        :param description: The description of this OperationDisplay.
        :param operation: The operation of this OperationDisplay.
        :param provider: The provider of this OperationDisplay.
        :param resource: The resource of this OperationDisplay.
        """
        self.openapi_types = {
            'description': str,
            'operation': str,
            'provider': str,
            'resource': str
        }

        self.attribute_map = {
            'description': 'description',
            'operation': 'operation',
            'provider': 'provider',
            'resource': 'resource'
        }

        self._description = description
        self._operation = operation
        self._provider = provider
        self._resource = resource

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OperationDisplay':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OperationDisplay of this OperationDisplay.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this OperationDisplay.

        Description of the operation to be performed.

        :return: The description of this OperationDisplay.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OperationDisplay.

        Description of the operation to be performed.

        :param description: The description of this OperationDisplay.
        :type description: str
        """

        self._description = description

    @property
    def operation(self):
        """Gets the operation of this OperationDisplay.

        Operation to be performed on the resource.

        :return: The operation of this OperationDisplay.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this OperationDisplay.

        Operation to be performed on the resource.

        :param operation: The operation of this OperationDisplay.
        :type operation: str
        """

        self._operation = operation

    @property
    def provider(self):
        """Gets the provider of this OperationDisplay.

        Provider name.

        :return: The provider of this OperationDisplay.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this OperationDisplay.

        Provider name.

        :param provider: The provider of this OperationDisplay.
        :type provider: str
        """

        self._provider = provider

    @property
    def resource(self):
        """Gets the resource of this OperationDisplay.

        The type of resource in which the operation is performed.

        :return: The resource of this OperationDisplay.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this OperationDisplay.

        The type of resource in which the operation is performed.

        :param resource: The resource of this OperationDisplay.
        :type resource: str
        """

        self._resource = resource
