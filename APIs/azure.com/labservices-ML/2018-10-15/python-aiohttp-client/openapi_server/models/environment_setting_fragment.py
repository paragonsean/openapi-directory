# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.environment_setting_properties_fragment import EnvironmentSettingPropertiesFragment
from openapi_server import util


class EnvironmentSettingFragment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, properties: EnvironmentSettingPropertiesFragment=None, id: str=None, location: str=None, name: str=None, tags: Dict[str, str]=None, type: str=None):
        """EnvironmentSettingFragment - a model defined in OpenAPI

        :param properties: The properties of this EnvironmentSettingFragment.
        :param id: The id of this EnvironmentSettingFragment.
        :param location: The location of this EnvironmentSettingFragment.
        :param name: The name of this EnvironmentSettingFragment.
        :param tags: The tags of this EnvironmentSettingFragment.
        :param type: The type of this EnvironmentSettingFragment.
        """
        self.openapi_types = {
            'properties': EnvironmentSettingPropertiesFragment,
            'id': str,
            'location': str,
            'name': str,
            'tags': Dict[str, str],
            'type': str
        }

        self.attribute_map = {
            'properties': 'properties',
            'id': 'id',
            'location': 'location',
            'name': 'name',
            'tags': 'tags',
            'type': 'type'
        }

        self._properties = properties
        self._id = id
        self._location = location
        self._name = name
        self._tags = tags
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EnvironmentSettingFragment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EnvironmentSettingFragment of this EnvironmentSettingFragment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def properties(self):
        """Gets the properties of this EnvironmentSettingFragment.


        :return: The properties of this EnvironmentSettingFragment.
        :rtype: EnvironmentSettingPropertiesFragment
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this EnvironmentSettingFragment.


        :param properties: The properties of this EnvironmentSettingFragment.
        :type properties: EnvironmentSettingPropertiesFragment
        """

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this EnvironmentSettingFragment.

        The identifier of the resource.

        :return: The id of this EnvironmentSettingFragment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnvironmentSettingFragment.

        The identifier of the resource.

        :param id: The id of this EnvironmentSettingFragment.
        :type id: str
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this EnvironmentSettingFragment.

        The location of the resource.

        :return: The location of this EnvironmentSettingFragment.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this EnvironmentSettingFragment.

        The location of the resource.

        :param location: The location of this EnvironmentSettingFragment.
        :type location: str
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this EnvironmentSettingFragment.

        The name of the resource.

        :return: The name of this EnvironmentSettingFragment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvironmentSettingFragment.

        The name of the resource.

        :param name: The name of this EnvironmentSettingFragment.
        :type name: str
        """

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this EnvironmentSettingFragment.

        The tags of the resource.

        :return: The tags of this EnvironmentSettingFragment.
        :rtype: Dict[str, str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EnvironmentSettingFragment.

        The tags of the resource.

        :param tags: The tags of this EnvironmentSettingFragment.
        :type tags: Dict[str, str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this EnvironmentSettingFragment.

        The type of the resource.

        :return: The type of this EnvironmentSettingFragment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EnvironmentSettingFragment.

        The type of the resource.

        :param type: The type of this EnvironmentSettingFragment.
        :type type: str
        """

        self._type = type
