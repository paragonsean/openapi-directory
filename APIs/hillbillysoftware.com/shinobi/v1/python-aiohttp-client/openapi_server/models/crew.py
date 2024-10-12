# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.external_ids import ExternalIDs
from openapi_server import util


class Crew(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, externals: List[ExternalIDs]=None, image: str=None, name: str=None, show_name: str=None, type: str=None):
        """Crew - a model defined in OpenAPI

        :param externals: The externals of this Crew.
        :param image: The image of this Crew.
        :param name: The name of this Crew.
        :param show_name: The show_name of this Crew.
        :param type: The type of this Crew.
        """
        self.openapi_types = {
            'externals': List[ExternalIDs],
            'image': str,
            'name': str,
            'show_name': str,
            'type': str
        }

        self.attribute_map = {
            'externals': 'Externals',
            'image': 'Image',
            'name': 'Name',
            'show_name': 'ShowName',
            'type': 'Type'
        }

        self._externals = externals
        self._image = image
        self._name = name
        self._show_name = show_name
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Crew':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Crew of this Crew.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def externals(self):
        """Gets the externals of this Crew.


        :return: The externals of this Crew.
        :rtype: List[ExternalIDs]
        """
        return self._externals

    @externals.setter
    def externals(self, externals):
        """Sets the externals of this Crew.


        :param externals: The externals of this Crew.
        :type externals: List[ExternalIDs]
        """

        self._externals = externals

    @property
    def image(self):
        """Gets the image of this Crew.


        :return: The image of this Crew.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Crew.


        :param image: The image of this Crew.
        :type image: str
        """

        self._image = image

    @property
    def name(self):
        """Gets the name of this Crew.


        :return: The name of this Crew.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Crew.


        :param name: The name of this Crew.
        :type name: str
        """

        self._name = name

    @property
    def show_name(self):
        """Gets the show_name of this Crew.


        :return: The show_name of this Crew.
        :rtype: str
        """
        return self._show_name

    @show_name.setter
    def show_name(self, show_name):
        """Sets the show_name of this Crew.


        :param show_name: The show_name of this Crew.
        :type show_name: str
        """

        self._show_name = show_name

    @property
    def type(self):
        """Gets the type of this Crew.


        :return: The type of this Crew.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Crew.


        :param type: The type of this Crew.
        :type type: str
        """

        self._type = type
