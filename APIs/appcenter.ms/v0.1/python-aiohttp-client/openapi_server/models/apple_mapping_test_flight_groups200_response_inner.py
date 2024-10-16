# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AppleMappingTestFlightGroups200ResponseInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, apple_id: float=None, id: str=None, name: str=None, provider_id: float=None):
        """AppleMappingTestFlightGroups200ResponseInner - a model defined in OpenAPI

        :param apple_id: The apple_id of this AppleMappingTestFlightGroups200ResponseInner.
        :param id: The id of this AppleMappingTestFlightGroups200ResponseInner.
        :param name: The name of this AppleMappingTestFlightGroups200ResponseInner.
        :param provider_id: The provider_id of this AppleMappingTestFlightGroups200ResponseInner.
        """
        self.openapi_types = {
            'apple_id': float,
            'id': str,
            'name': str,
            'provider_id': float
        }

        self.attribute_map = {
            'apple_id': 'appleId',
            'id': 'id',
            'name': 'name',
            'provider_id': 'providerId'
        }

        self._apple_id = apple_id
        self._id = id
        self._name = name
        self._provider_id = provider_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AppleMappingTestFlightGroups200ResponseInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The appleMapping_TestFlightGroups_200_response_inner of this AppleMappingTestFlightGroups200ResponseInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def apple_id(self):
        """Gets the apple_id of this AppleMappingTestFlightGroups200ResponseInner.

        apple id of the group.

        :return: The apple_id of this AppleMappingTestFlightGroups200ResponseInner.
        :rtype: float
        """
        return self._apple_id

    @apple_id.setter
    def apple_id(self, apple_id):
        """Sets the apple_id of this AppleMappingTestFlightGroups200ResponseInner.

        apple id of the group.

        :param apple_id: The apple_id of this AppleMappingTestFlightGroups200ResponseInner.
        :type apple_id: float
        """

        self._apple_id = apple_id

    @property
    def id(self):
        """Gets the id of this AppleMappingTestFlightGroups200ResponseInner.

        id of the group.

        :return: The id of this AppleMappingTestFlightGroups200ResponseInner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppleMappingTestFlightGroups200ResponseInner.

        id of the group.

        :param id: The id of this AppleMappingTestFlightGroups200ResponseInner.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AppleMappingTestFlightGroups200ResponseInner.

        name of the group.

        :return: The name of this AppleMappingTestFlightGroups200ResponseInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppleMappingTestFlightGroups200ResponseInner.

        name of the group.

        :param name: The name of this AppleMappingTestFlightGroups200ResponseInner.
        :type name: str
        """

        self._name = name

    @property
    def provider_id(self):
        """Gets the provider_id of this AppleMappingTestFlightGroups200ResponseInner.

        provider id of the group.

        :return: The provider_id of this AppleMappingTestFlightGroups200ResponseInner.
        :rtype: float
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this AppleMappingTestFlightGroups200ResponseInner.

        provider id of the group.

        :param provider_id: The provider_id of this AppleMappingTestFlightGroups200ResponseInner.
        :type provider_id: float
        """

        self._provider_id = provider_id
