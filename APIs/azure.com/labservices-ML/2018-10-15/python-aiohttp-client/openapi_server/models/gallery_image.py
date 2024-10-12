# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.gallery_image_properties import GalleryImageProperties
from openapi_server import util


class GalleryImage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, properties: GalleryImageProperties=None, id: str=None, location: str=None, name: str=None, tags: Dict[str, str]=None, type: str=None):
        """GalleryImage - a model defined in OpenAPI

        :param properties: The properties of this GalleryImage.
        :param id: The id of this GalleryImage.
        :param location: The location of this GalleryImage.
        :param name: The name of this GalleryImage.
        :param tags: The tags of this GalleryImage.
        :param type: The type of this GalleryImage.
        """
        self.openapi_types = {
            'properties': GalleryImageProperties,
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
    def from_dict(cls, dikt: dict) -> 'GalleryImage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GalleryImage of this GalleryImage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def properties(self):
        """Gets the properties of this GalleryImage.


        :return: The properties of this GalleryImage.
        :rtype: GalleryImageProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GalleryImage.


        :param properties: The properties of this GalleryImage.
        :type properties: GalleryImageProperties
        """

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this GalleryImage.

        The identifier of the resource.

        :return: The id of this GalleryImage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GalleryImage.

        The identifier of the resource.

        :param id: The id of this GalleryImage.
        :type id: str
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this GalleryImage.

        The location of the resource.

        :return: The location of this GalleryImage.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this GalleryImage.

        The location of the resource.

        :param location: The location of this GalleryImage.
        :type location: str
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this GalleryImage.

        The name of the resource.

        :return: The name of this GalleryImage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GalleryImage.

        The name of the resource.

        :param name: The name of this GalleryImage.
        :type name: str
        """

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this GalleryImage.

        The tags of the resource.

        :return: The tags of this GalleryImage.
        :rtype: Dict[str, str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GalleryImage.

        The tags of the resource.

        :param tags: The tags of this GalleryImage.
        :type tags: Dict[str, str]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this GalleryImage.

        The type of the resource.

        :return: The type of this GalleryImage.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GalleryImage.

        The type of the resource.

        :param type: The type of this GalleryImage.
        :type type: str
        """

        self._type = type
