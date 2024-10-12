# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class VersionSpec(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, component_versions: Dict[str, str]=None, display_name: str=None, friendly_name: str=None, is_default: str=None):
        """VersionSpec - a model defined in OpenAPI

        :param component_versions: The component_versions of this VersionSpec.
        :param display_name: The display_name of this VersionSpec.
        :param friendly_name: The friendly_name of this VersionSpec.
        :param is_default: The is_default of this VersionSpec.
        """
        self.openapi_types = {
            'component_versions': Dict[str, str],
            'display_name': str,
            'friendly_name': str,
            'is_default': str
        }

        self.attribute_map = {
            'component_versions': 'componentVersions',
            'display_name': 'displayName',
            'friendly_name': 'friendlyName',
            'is_default': 'isDefault'
        }

        self._component_versions = component_versions
        self._display_name = display_name
        self._friendly_name = friendly_name
        self._is_default = is_default

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VersionSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The versionSpec of this VersionSpec.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def component_versions(self):
        """Gets the component_versions of this VersionSpec.

        The component version property.

        :return: The component_versions of this VersionSpec.
        :rtype: Dict[str, str]
        """
        return self._component_versions

    @component_versions.setter
    def component_versions(self, component_versions):
        """Sets the component_versions of this VersionSpec.

        The component version property.

        :param component_versions: The component_versions of this VersionSpec.
        :type component_versions: Dict[str, str]
        """

        self._component_versions = component_versions

    @property
    def display_name(self):
        """Gets the display_name of this VersionSpec.

        The display name

        :return: The display_name of this VersionSpec.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this VersionSpec.

        The display name

        :param display_name: The display_name of this VersionSpec.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def friendly_name(self):
        """Gets the friendly_name of this VersionSpec.

        The friendly name

        :return: The friendly_name of this VersionSpec.
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """Sets the friendly_name of this VersionSpec.

        The friendly name

        :param friendly_name: The friendly_name of this VersionSpec.
        :type friendly_name: str
        """

        self._friendly_name = friendly_name

    @property
    def is_default(self):
        """Gets the is_default of this VersionSpec.

        Whether or not the version is the default version.

        :return: The is_default of this VersionSpec.
        :rtype: str
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this VersionSpec.

        Whether or not the version is the default version.

        :param is_default: The is_default of this VersionSpec.
        :type is_default: str
        """

        self._is_default = is_default
