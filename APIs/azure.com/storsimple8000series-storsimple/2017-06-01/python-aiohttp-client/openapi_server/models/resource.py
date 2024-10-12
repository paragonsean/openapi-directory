# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Resource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, location: str=None, name: str=None, tags: Dict[str, str]=None, type: str=None):
        """Resource - a model defined in OpenAPI

        :param id: The id of this Resource.
        :param location: The location of this Resource.
        :param name: The name of this Resource.
        :param tags: The tags of this Resource.
        :param type: The type of this Resource.
        """
        self.openapi_types = {
            'id': str,
            'location': str,
            'name': str,
            'tags': Dict[str, str],
            'type': str
        }

        self.attribute_map = {
            'id': 'id',
            'location': 'location',
            'name': 'name',
            'tags': 'tags',
            'type': 'type'
        }

        self._id = id
        self._location = location
        self._name = name
        self._tags = tags
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Resource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Resource of this Resource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Resource.

        The resource ID.

        :return: The id of this Resource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Resource.

        The resource ID.

        :param id: The id of this Resource.
        :type id: str
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this Resource.

        The geo location of the resource.

        :return: The location of this Resource.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Resource.

        The geo location of the resource.

        :param location: The location of this Resource.
        :type location: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")

        self._location = location

    @property
    def name(self):
        """Gets the name of this Resource.

        The resource name.

        :return: The name of this Resource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Resource.

        The resource name.

        :param name: The name of this Resource.
        :type name: str
        """

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this Resource.

        The tags attached to the resource.

        :return: The tags of this Resource.
        :rtype: Dict[str, str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Resource.

        The tags attached to the resource.

        :param tags: The tags of this Resource.
        :type tags: Dict[str, str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this Resource.

        The resource type.

        :return: The type of this Resource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Resource.

        The resource type.

        :param type: The type of this Resource.
        :type type: str
        """

        self._type = type
