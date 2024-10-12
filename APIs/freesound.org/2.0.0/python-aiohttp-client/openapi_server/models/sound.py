# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Sound(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, url: str=None):
        """Sound - a model defined in OpenAPI

        :param id: The id of this Sound.
        :param name: The name of this Sound.
        :param url: The url of this Sound.
        """
        self.openapi_types = {
            'id': int,
            'name': str,
            'url': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'url': 'url'
        }

        self._id = id
        self._name = name
        self._url = url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Sound':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Sound of this Sound.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Sound.

        The sound’s unique identifier.

        :return: The id of this Sound.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Sound.

        The sound’s unique identifier.

        :param id: The id of this Sound.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Sound.

        The name user gave to the sound.

        :return: The name of this Sound.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Sound.

        The name user gave to the sound.

        :param name: The name of this Sound.
        :type name: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this Sound.

        The URI for this sound on the Freesound website.

        :return: The url of this Sound.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Sound.

        The URI for this sound on the Freesound website.

        :param url: The url of this Sound.
        :type url: str
        """

        self._url = url
