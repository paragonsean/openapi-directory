# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ProviderOperation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, display_name: str=None, is_data_action: bool=None, name: str=None, origin: str=None, properties: object=None):
        """ProviderOperation - a model defined in OpenAPI

        :param description: The description of this ProviderOperation.
        :param display_name: The display_name of this ProviderOperation.
        :param is_data_action: The is_data_action of this ProviderOperation.
        :param name: The name of this ProviderOperation.
        :param origin: The origin of this ProviderOperation.
        :param properties: The properties of this ProviderOperation.
        """
        self.openapi_types = {
            'description': str,
            'display_name': str,
            'is_data_action': bool,
            'name': str,
            'origin': str,
            'properties': object
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'is_data_action': 'isDataAction',
            'name': 'name',
            'origin': 'origin',
            'properties': 'properties'
        }

        self._description = description
        self._display_name = display_name
        self._is_data_action = is_data_action
        self._name = name
        self._origin = origin
        self._properties = properties

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProviderOperation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProviderOperation of this ProviderOperation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this ProviderOperation.

        The operation description.

        :return: The description of this ProviderOperation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProviderOperation.

        The operation description.

        :param description: The description of this ProviderOperation.
        :type description: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this ProviderOperation.

        The operation display name.

        :return: The display_name of this ProviderOperation.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ProviderOperation.

        The operation display name.

        :param display_name: The display_name of this ProviderOperation.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def is_data_action(self):
        """Gets the is_data_action of this ProviderOperation.

        The dataAction flag to specify the operation type.

        :return: The is_data_action of this ProviderOperation.
        :rtype: bool
        """
        return self._is_data_action

    @is_data_action.setter
    def is_data_action(self, is_data_action):
        """Sets the is_data_action of this ProviderOperation.

        The dataAction flag to specify the operation type.

        :param is_data_action: The is_data_action of this ProviderOperation.
        :type is_data_action: bool
        """

        self._is_data_action = is_data_action

    @property
    def name(self):
        """Gets the name of this ProviderOperation.

        The operation name.

        :return: The name of this ProviderOperation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProviderOperation.

        The operation name.

        :param name: The name of this ProviderOperation.
        :type name: str
        """

        self._name = name

    @property
    def origin(self):
        """Gets the origin of this ProviderOperation.

        The operation origin.

        :return: The origin of this ProviderOperation.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this ProviderOperation.

        The operation origin.

        :param origin: The origin of this ProviderOperation.
        :type origin: str
        """

        self._origin = origin

    @property
    def properties(self):
        """Gets the properties of this ProviderOperation.

        The operation properties.

        :return: The properties of this ProviderOperation.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ProviderOperation.

        The operation properties.

        :param properties: The properties of this ProviderOperation.
        :type properties: object
        """

        self._properties = properties
