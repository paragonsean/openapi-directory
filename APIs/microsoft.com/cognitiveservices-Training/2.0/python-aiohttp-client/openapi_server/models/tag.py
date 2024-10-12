# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Tag(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, id: str=None, image_count: int=None, name: str=None):
        """Tag - a model defined in OpenAPI

        :param description: The description of this Tag.
        :param id: The id of this Tag.
        :param image_count: The image_count of this Tag.
        :param name: The name of this Tag.
        """
        self.openapi_types = {
            'description': str,
            'id': str,
            'image_count': int,
            'name': str
        }

        self.attribute_map = {
            'description': 'description',
            'id': 'id',
            'image_count': 'imageCount',
            'name': 'name'
        }

        self._description = description
        self._id = id
        self._image_count = image_count
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Tag':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Tag of this Tag.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this Tag.

        Gets or sets the description of the tag

        :return: The description of this Tag.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Tag.

        Gets or sets the description of the tag

        :param description: The description of this Tag.
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Tag.

        Gets the Tag ID

        :return: The id of this Tag.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tag.

        Gets the Tag ID

        :param id: The id of this Tag.
        :type id: str
        """

        self._id = id

    @property
    def image_count(self):
        """Gets the image_count of this Tag.

        Gets the number of images with this tag

        :return: The image_count of this Tag.
        :rtype: int
        """
        return self._image_count

    @image_count.setter
    def image_count(self, image_count):
        """Sets the image_count of this Tag.

        Gets the number of images with this tag

        :param image_count: The image_count of this Tag.
        :type image_count: int
        """

        self._image_count = image_count

    @property
    def name(self):
        """Gets the name of this Tag.

        Gets or sets the name of the tag

        :return: The name of this Tag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tag.

        Gets or sets the name of the tag

        :param name: The name of this Tag.
        :type name: str
        """

        self._name = name
