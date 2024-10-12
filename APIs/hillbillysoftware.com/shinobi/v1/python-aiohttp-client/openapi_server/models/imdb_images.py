# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ImdbImages(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, backdrops: List[str]=None, posters: List[str]=None, type: str=None, imdb_id: str=None):
        """ImdbImages - a model defined in OpenAPI

        :param backdrops: The backdrops of this ImdbImages.
        :param posters: The posters of this ImdbImages.
        :param type: The type of this ImdbImages.
        :param imdb_id: The imdb_id of this ImdbImages.
        """
        self.openapi_types = {
            'backdrops': List[str],
            'posters': List[str],
            'type': str,
            'imdb_id': str
        }

        self.attribute_map = {
            'backdrops': 'Backdrops',
            'posters': 'Posters',
            'type': 'Type',
            'imdb_id': 'imdbID'
        }

        self._backdrops = backdrops
        self._posters = posters
        self._type = type
        self._imdb_id = imdb_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ImdbImages':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The imdbImages of this ImdbImages.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def backdrops(self):
        """Gets the backdrops of this ImdbImages.


        :return: The backdrops of this ImdbImages.
        :rtype: List[str]
        """
        return self._backdrops

    @backdrops.setter
    def backdrops(self, backdrops):
        """Sets the backdrops of this ImdbImages.


        :param backdrops: The backdrops of this ImdbImages.
        :type backdrops: List[str]
        """

        self._backdrops = backdrops

    @property
    def posters(self):
        """Gets the posters of this ImdbImages.


        :return: The posters of this ImdbImages.
        :rtype: List[str]
        """
        return self._posters

    @posters.setter
    def posters(self, posters):
        """Sets the posters of this ImdbImages.


        :param posters: The posters of this ImdbImages.
        :type posters: List[str]
        """

        self._posters = posters

    @property
    def type(self):
        """Gets the type of this ImdbImages.


        :return: The type of this ImdbImages.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImdbImages.


        :param type: The type of this ImdbImages.
        :type type: str
        """

        self._type = type

    @property
    def imdb_id(self):
        """Gets the imdb_id of this ImdbImages.


        :return: The imdb_id of this ImdbImages.
        :rtype: str
        """
        return self._imdb_id

    @imdb_id.setter
    def imdb_id(self, imdb_id):
        """Sets the imdb_id of this ImdbImages.


        :param imdb_id: The imdb_id of this ImdbImages.
        :type imdb_id: str
        """

        self._imdb_id = imdb_id
