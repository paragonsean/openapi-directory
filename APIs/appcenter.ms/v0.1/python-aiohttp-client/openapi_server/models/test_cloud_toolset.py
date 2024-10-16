# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.builds_list_toolset_projects200_response_testcloud_projects_inner import BuildsListToolsetProjects200ResponseTestcloudProjectsInner
from openapi_server import util


class TestCloudToolset(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, projects: List[BuildsListToolsetProjects200ResponseTestcloudProjectsInner]=None):
        """TestCloudToolset - a model defined in OpenAPI

        :param projects: The projects of this TestCloudToolset.
        """
        self.openapi_types = {
            'projects': List[BuildsListToolsetProjects200ResponseTestcloudProjectsInner]
        }

        self.attribute_map = {
            'projects': 'projects'
        }

        self._projects = projects

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TestCloudToolset':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TestCloudToolset of this TestCloudToolset.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def projects(self):
        """Gets the projects of this TestCloudToolset.

        The TestCloud projects detected

        :return: The projects of this TestCloudToolset.
        :rtype: List[BuildsListToolsetProjects200ResponseTestcloudProjectsInner]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this TestCloudToolset.

        The TestCloud projects detected

        :param projects: The projects of this TestCloudToolset.
        :type projects: List[BuildsListToolsetProjects200ResponseTestcloudProjectsInner]
        """
        if projects is None:
            raise ValueError("Invalid value for `projects`, must not be `None`")

        self._projects = projects
