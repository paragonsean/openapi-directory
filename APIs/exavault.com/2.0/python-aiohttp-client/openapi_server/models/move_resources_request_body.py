# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class MoveResourcesRequestBody(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, parent_resource: str=None, resources: List[str]=None):
        """MoveResourcesRequestBody - a model defined in OpenAPI

        :param parent_resource: The parent_resource of this MoveResourcesRequestBody.
        :param resources: The resources of this MoveResourcesRequestBody.
        """
        self.openapi_types = {
            'parent_resource': str,
            'resources': List[str]
        }

        self.attribute_map = {
            'parent_resource': 'parentResource',
            'resources': 'resources'
        }

        self._parent_resource = parent_resource
        self._resources = resources

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MoveResourcesRequestBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MoveResourcesRequestBody of this MoveResourcesRequestBody.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def parent_resource(self):
        """Gets the parent_resource of this MoveResourcesRequestBody.

        Resource identifier of folder to move files/folders to.

        :return: The parent_resource of this MoveResourcesRequestBody.
        :rtype: str
        """
        return self._parent_resource

    @parent_resource.setter
    def parent_resource(self, parent_resource):
        """Sets the parent_resource of this MoveResourcesRequestBody.

        Resource identifier of folder to move files/folders to.

        :param parent_resource: The parent_resource of this MoveResourcesRequestBody.
        :type parent_resource: str
        """
        if parent_resource is None:
            raise ValueError("Invalid value for `parent_resource`, must not be `None`")

        self._parent_resource = parent_resource

    @property
    def resources(self):
        """Gets the resources of this MoveResourcesRequestBody.

        Array containing file/folder paths to move.

        :return: The resources of this MoveResourcesRequestBody.
        :rtype: List[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this MoveResourcesRequestBody.

        Array containing file/folder paths to move.

        :param resources: The resources of this MoveResourcesRequestBody.
        :type resources: List[str]
        """
        if resources is None:
            raise ValueError("Invalid value for `resources`, must not be `None`")

        self._resources = resources
