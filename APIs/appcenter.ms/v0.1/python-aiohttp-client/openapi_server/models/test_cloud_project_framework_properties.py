# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TestCloudProjectFrameworkProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, configurations: List[str]=None):
        """TestCloudProjectFrameworkProperties - a model defined in OpenAPI

        :param configurations: The configurations of this TestCloudProjectFrameworkProperties.
        """
        self.openapi_types = {
            'configurations': List[str]
        }

        self.attribute_map = {
            'configurations': 'configurations'
        }

        self._configurations = configurations

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TestCloudProjectFrameworkProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TestCloudProjectFrameworkProperties of this TestCloudProjectFrameworkProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def configurations(self):
        """Gets the configurations of this TestCloudProjectFrameworkProperties.


        :return: The configurations of this TestCloudProjectFrameworkProperties.
        :rtype: List[str]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """Sets the configurations of this TestCloudProjectFrameworkProperties.


        :param configurations: The configurations of this TestCloudProjectFrameworkProperties.
        :type configurations: List[str]
        """

        self._configurations = configurations
