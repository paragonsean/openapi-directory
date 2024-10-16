# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class MovieInformation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, imdb_id: str=None, release_year: str=None, runtime: str=None, synopsis: str=None, title: str=None):
        """MovieInformation - a model defined in OpenAPI

        :param id: The id of this MovieInformation.
        :param imdb_id: The imdb_id of this MovieInformation.
        :param release_year: The release_year of this MovieInformation.
        :param runtime: The runtime of this MovieInformation.
        :param synopsis: The synopsis of this MovieInformation.
        :param title: The title of this MovieInformation.
        """
        self.openapi_types = {
            'id': str,
            'imdb_id': str,
            'release_year': str,
            'runtime': str,
            'synopsis': str,
            'title': str
        }

        self.attribute_map = {
            'id': 'ID',
            'imdb_id': 'ImdbID',
            'release_year': 'ReleaseYear',
            'runtime': 'Runtime',
            'synopsis': 'Synopsis',
            'title': 'Title'
        }

        self._id = id
        self._imdb_id = imdb_id
        self._release_year = release_year
        self._runtime = runtime
        self._synopsis = synopsis
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MovieInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MovieInformation of this MovieInformation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this MovieInformation.


        :return: The id of this MovieInformation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MovieInformation.


        :param id: The id of this MovieInformation.
        :type id: str
        """

        self._id = id

    @property
    def imdb_id(self):
        """Gets the imdb_id of this MovieInformation.


        :return: The imdb_id of this MovieInformation.
        :rtype: str
        """
        return self._imdb_id

    @imdb_id.setter
    def imdb_id(self, imdb_id):
        """Sets the imdb_id of this MovieInformation.


        :param imdb_id: The imdb_id of this MovieInformation.
        :type imdb_id: str
        """

        self._imdb_id = imdb_id

    @property
    def release_year(self):
        """Gets the release_year of this MovieInformation.


        :return: The release_year of this MovieInformation.
        :rtype: str
        """
        return self._release_year

    @release_year.setter
    def release_year(self, release_year):
        """Sets the release_year of this MovieInformation.


        :param release_year: The release_year of this MovieInformation.
        :type release_year: str
        """

        self._release_year = release_year

    @property
    def runtime(self):
        """Gets the runtime of this MovieInformation.


        :return: The runtime of this MovieInformation.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this MovieInformation.


        :param runtime: The runtime of this MovieInformation.
        :type runtime: str
        """

        self._runtime = runtime

    @property
    def synopsis(self):
        """Gets the synopsis of this MovieInformation.


        :return: The synopsis of this MovieInformation.
        :rtype: str
        """
        return self._synopsis

    @synopsis.setter
    def synopsis(self, synopsis):
        """Sets the synopsis of this MovieInformation.


        :param synopsis: The synopsis of this MovieInformation.
        :type synopsis: str
        """

        self._synopsis = synopsis

    @property
    def title(self):
        """Gets the title of this MovieInformation.


        :return: The title of this MovieInformation.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MovieInformation.


        :param title: The title of this MovieInformation.
        :type title: str
        """

        self._title = title
