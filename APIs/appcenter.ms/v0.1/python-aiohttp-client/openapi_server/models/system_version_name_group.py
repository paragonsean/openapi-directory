# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SystemVersionNameGroup(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, versions: List[str]=None):
        """SystemVersionNameGroup - a model defined in OpenAPI

        :param name: The name of this SystemVersionNameGroup.
        :param versions: The versions of this SystemVersionNameGroup.
        """
        self.openapi_types = {
            'name': str,
            'versions': List[str]
        }

        self.attribute_map = {
            'name': 'name',
            'versions': 'versions'
        }

        self._name = name
        self._versions = versions

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SystemVersionNameGroup':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SystemVersionNameGroup of this SystemVersionNameGroup.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this SystemVersionNameGroup.

        Name of version group

        :return: The name of this SystemVersionNameGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemVersionNameGroup.

        Name of version group

        :param name: The name of this SystemVersionNameGroup.
        :type name: str
        """

        self._name = name

    @property
    def versions(self):
        """Gets the versions of this SystemVersionNameGroup.


        :return: The versions of this SystemVersionNameGroup.
        :rtype: List[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this SystemVersionNameGroup.


        :param versions: The versions of this SystemVersionNameGroup.
        :type versions: List[str]
        """

        self._versions = versions
