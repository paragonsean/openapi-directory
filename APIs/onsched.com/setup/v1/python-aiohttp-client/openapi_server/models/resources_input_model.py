# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.resource_input_model import ResourceInputModel
from openapi_server import util


class ResourcesInputModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, resources: List[ResourceInputModel]=None):
        """ResourcesInputModel - a model defined in OpenAPI

        :param resources: The resources of this ResourcesInputModel.
        """
        self.openapi_types = {
            'resources': List[ResourceInputModel]
        }

        self.attribute_map = {
            'resources': 'resources'
        }

        self._resources = resources

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ResourcesInputModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ResourcesInputModel of this ResourcesInputModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resources(self):
        """Gets the resources of this ResourcesInputModel.


        :return: The resources of this ResourcesInputModel.
        :rtype: List[ResourceInputModel]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ResourcesInputModel.


        :param resources: The resources of this ResourcesInputModel.
        :type resources: List[ResourceInputModel]
        """

        self._resources = resources
