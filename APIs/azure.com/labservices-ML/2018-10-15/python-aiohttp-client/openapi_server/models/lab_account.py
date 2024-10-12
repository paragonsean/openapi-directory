# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.lab_account_properties import LabAccountProperties
from openapi_server import util


class LabAccount(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, properties: LabAccountProperties=None, id: str=None, location: str=None, name: str=None, tags: Dict[str, str]=None, type: str=None):
        """LabAccount - a model defined in OpenAPI

        :param properties: The properties of this LabAccount.
        :param id: The id of this LabAccount.
        :param location: The location of this LabAccount.
        :param name: The name of this LabAccount.
        :param tags: The tags of this LabAccount.
        :param type: The type of this LabAccount.
        """
        self.openapi_types = {
            'properties': LabAccountProperties,
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
    def from_dict(cls, dikt: dict) -> 'LabAccount':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LabAccount of this LabAccount.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def properties(self):
        """Gets the properties of this LabAccount.


        :return: The properties of this LabAccount.
        :rtype: LabAccountProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this LabAccount.


        :param properties: The properties of this LabAccount.
        :type properties: LabAccountProperties
        """

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this LabAccount.

        The identifier of the resource.

        :return: The id of this LabAccount.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LabAccount.

        The identifier of the resource.

        :param id: The id of this LabAccount.
        :type id: str
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this LabAccount.

        The location of the resource.

        :return: The location of this LabAccount.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this LabAccount.

        The location of the resource.

        :param location: The location of this LabAccount.
        :type location: str
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this LabAccount.

        The name of the resource.

        :return: The name of this LabAccount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LabAccount.

        The name of the resource.

        :param name: The name of this LabAccount.
        :type name: str
        """

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this LabAccount.

        The tags of the resource.

        :return: The tags of this LabAccount.
        :rtype: Dict[str, str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this LabAccount.

        The tags of the resource.

        :param tags: The tags of this LabAccount.
        :type tags: Dict[str, str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this LabAccount.

        The type of the resource.

        :return: The type of this LabAccount.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LabAccount.

        The type of the resource.

        :param type: The type of this LabAccount.
        :type type: str
        """

        self._type = type
