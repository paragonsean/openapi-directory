# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class WatchedDirectory(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, path: str=None):
        """WatchedDirectory - a model defined in OpenAPI

        :param id: The id of this WatchedDirectory.
        :param path: The path of this WatchedDirectory.
        """
        self.openapi_types = {
            'id': int,
            'path': str
        }

        self.attribute_map = {
            'id': 'id',
            'path': 'path'
        }

        self._id = id
        self._path = path

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WatchedDirectory':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The watchedDirectory of this WatchedDirectory.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this WatchedDirectory.


        :return: The id of this WatchedDirectory.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WatchedDirectory.


        :param id: The id of this WatchedDirectory.
        :type id: int
        """

        self._id = id

    @property
    def path(self):
        """Gets the path of this WatchedDirectory.


        :return: The path of this WatchedDirectory.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this WatchedDirectory.


        :param path: The path of this WatchedDirectory.
        :type path: str
        """

        self._path = path
