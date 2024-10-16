# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.videogame_id import VideogameID
from openapi_server import util


class VideogameTitle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, videogame_id: VideogameID=None):
        """VideogameTitle - a model defined in OpenAPI

        :param id: The id of this VideogameTitle.
        :param name: The name of this VideogameTitle.
        :param videogame_id: The videogame_id of this VideogameTitle.
        """
        self.openapi_types = {
            'id': int,
            'name': str,
            'videogame_id': VideogameID
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'videogame_id': 'videogame_id'
        }

        self._id = id
        self._name = name
        self._videogame_id = videogame_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VideogameTitle':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VideogameTitle of this VideogameTitle.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this VideogameTitle.


        :return: The id of this VideogameTitle.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VideogameTitle.


        :param id: The id of this VideogameTitle.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        if id is not None and id < 1:
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this VideogameTitle.


        :return: The name of this VideogameTitle.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VideogameTitle.


        :param name: The name of this VideogameTitle.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def videogame_id(self):
        """Gets the videogame_id of this VideogameTitle.


        :return: The videogame_id of this VideogameTitle.
        :rtype: VideogameID
        """
        return self._videogame_id

    @videogame_id.setter
    def videogame_id(self, videogame_id):
        """Sets the videogame_id of this VideogameTitle.


        :param videogame_id: The videogame_id of this VideogameTitle.
        :type videogame_id: VideogameID
        """
        if videogame_id is None:
            raise ValueError("Invalid value for `videogame_id`, must not be `None`")

        self._videogame_id = videogame_id
