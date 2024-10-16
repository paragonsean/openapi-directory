# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.builds_list_toolset_projects200_response_testcloud_projects_inner_framework_properties import BuildsListToolsetProjects200ResponseTestcloudProjectsInnerFrameworkProperties
from openapi_server import util


class TestCloudProject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, framework_properties: BuildsListToolsetProjects200ResponseTestcloudProjectsInnerFrameworkProperties=None, framework_type: str=None, path: str=None):
        """TestCloudProject - a model defined in OpenAPI

        :param framework_properties: The framework_properties of this TestCloudProject.
        :param framework_type: The framework_type of this TestCloudProject.
        :param path: The path of this TestCloudProject.
        """
        self.openapi_types = {
            'framework_properties': BuildsListToolsetProjects200ResponseTestcloudProjectsInnerFrameworkProperties,
            'framework_type': str,
            'path': str
        }

        self.attribute_map = {
            'framework_properties': 'frameworkProperties',
            'framework_type': 'frameworkType',
            'path': 'path'
        }

        self._framework_properties = framework_properties
        self._framework_type = framework_type
        self._path = path

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TestCloudProject':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TestCloudProject of this TestCloudProject.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def framework_properties(self):
        """Gets the framework_properties of this TestCloudProject.


        :return: The framework_properties of this TestCloudProject.
        :rtype: BuildsListToolsetProjects200ResponseTestcloudProjectsInnerFrameworkProperties
        """
        return self._framework_properties

    @framework_properties.setter
    def framework_properties(self, framework_properties):
        """Sets the framework_properties of this TestCloudProject.


        :param framework_properties: The framework_properties of this TestCloudProject.
        :type framework_properties: BuildsListToolsetProjects200ResponseTestcloudProjectsInnerFrameworkProperties
        """

        self._framework_properties = framework_properties

    @property
    def framework_type(self):
        """Gets the framework_type of this TestCloudProject.


        :return: The framework_type of this TestCloudProject.
        :rtype: str
        """
        return self._framework_type

    @framework_type.setter
    def framework_type(self, framework_type):
        """Sets the framework_type of this TestCloudProject.


        :param framework_type: The framework_type of this TestCloudProject.
        :type framework_type: str
        """
        allowed_values = ["Appium", "Calabash", "Espresso", "UITest", "Generated"]  # noqa: E501
        if framework_type not in allowed_values:
            raise ValueError(
                "Invalid value for `framework_type` ({0}), must be one of {1}"
                .format(framework_type, allowed_values)
            )

        self._framework_type = framework_type

    @property
    def path(self):
        """Gets the path of this TestCloudProject.

        The path to the TestCloud project

        :return: The path of this TestCloudProject.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this TestCloudProject.

        The path to the TestCloud project

        :param path: The path of this TestCloudProject.
        :type path: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")

        self._path = path
