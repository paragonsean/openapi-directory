# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TVInformationPost(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access_token: str=None, episode_count: str=None, episode_runtime: str=None, genres: str=None, imdb_id: str=None, premier_year: str=None, seasons: str=None, show_image: str=None, show_status: str=None, synopsis: str=None, title: str=None):
        """TVInformationPost - a model defined in OpenAPI

        :param access_token: The access_token of this TVInformationPost.
        :param episode_count: The episode_count of this TVInformationPost.
        :param episode_runtime: The episode_runtime of this TVInformationPost.
        :param genres: The genres of this TVInformationPost.
        :param imdb_id: The imdb_id of this TVInformationPost.
        :param premier_year: The premier_year of this TVInformationPost.
        :param seasons: The seasons of this TVInformationPost.
        :param show_image: The show_image of this TVInformationPost.
        :param show_status: The show_status of this TVInformationPost.
        :param synopsis: The synopsis of this TVInformationPost.
        :param title: The title of this TVInformationPost.
        """
        self.openapi_types = {
            'access_token': str,
            'episode_count': str,
            'episode_runtime': str,
            'genres': str,
            'imdb_id': str,
            'premier_year': str,
            'seasons': str,
            'show_image': str,
            'show_status': str,
            'synopsis': str,
            'title': str
        }

        self.attribute_map = {
            'access_token': 'AccessToken',
            'episode_count': 'EpisodeCount',
            'episode_runtime': 'EpisodeRuntime',
            'genres': 'Genres',
            'imdb_id': 'ImdbID',
            'premier_year': 'PremierYear',
            'seasons': 'Seasons',
            'show_image': 'ShowImage',
            'show_status': 'ShowStatus',
            'synopsis': 'Synopsis',
            'title': 'Title'
        }

        self._access_token = access_token
        self._episode_count = episode_count
        self._episode_runtime = episode_runtime
        self._genres = genres
        self._imdb_id = imdb_id
        self._premier_year = premier_year
        self._seasons = seasons
        self._show_image = show_image
        self._show_status = show_status
        self._synopsis = synopsis
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TVInformationPost':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TVInformationPost of this TVInformationPost.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_token(self):
        """Gets the access_token of this TVInformationPost.


        :return: The access_token of this TVInformationPost.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this TVInformationPost.


        :param access_token: The access_token of this TVInformationPost.
        :type access_token: str
        """

        self._access_token = access_token

    @property
    def episode_count(self):
        """Gets the episode_count of this TVInformationPost.


        :return: The episode_count of this TVInformationPost.
        :rtype: str
        """
        return self._episode_count

    @episode_count.setter
    def episode_count(self, episode_count):
        """Sets the episode_count of this TVInformationPost.


        :param episode_count: The episode_count of this TVInformationPost.
        :type episode_count: str
        """

        self._episode_count = episode_count

    @property
    def episode_runtime(self):
        """Gets the episode_runtime of this TVInformationPost.


        :return: The episode_runtime of this TVInformationPost.
        :rtype: str
        """
        return self._episode_runtime

    @episode_runtime.setter
    def episode_runtime(self, episode_runtime):
        """Sets the episode_runtime of this TVInformationPost.


        :param episode_runtime: The episode_runtime of this TVInformationPost.
        :type episode_runtime: str
        """

        self._episode_runtime = episode_runtime

    @property
    def genres(self):
        """Gets the genres of this TVInformationPost.


        :return: The genres of this TVInformationPost.
        :rtype: str
        """
        return self._genres

    @genres.setter
    def genres(self, genres):
        """Sets the genres of this TVInformationPost.


        :param genres: The genres of this TVInformationPost.
        :type genres: str
        """

        self._genres = genres

    @property
    def imdb_id(self):
        """Gets the imdb_id of this TVInformationPost.


        :return: The imdb_id of this TVInformationPost.
        :rtype: str
        """
        return self._imdb_id

    @imdb_id.setter
    def imdb_id(self, imdb_id):
        """Sets the imdb_id of this TVInformationPost.


        :param imdb_id: The imdb_id of this TVInformationPost.
        :type imdb_id: str
        """

        self._imdb_id = imdb_id

    @property
    def premier_year(self):
        """Gets the premier_year of this TVInformationPost.


        :return: The premier_year of this TVInformationPost.
        :rtype: str
        """
        return self._premier_year

    @premier_year.setter
    def premier_year(self, premier_year):
        """Sets the premier_year of this TVInformationPost.


        :param premier_year: The premier_year of this TVInformationPost.
        :type premier_year: str
        """

        self._premier_year = premier_year

    @property
    def seasons(self):
        """Gets the seasons of this TVInformationPost.


        :return: The seasons of this TVInformationPost.
        :rtype: str
        """
        return self._seasons

    @seasons.setter
    def seasons(self, seasons):
        """Sets the seasons of this TVInformationPost.


        :param seasons: The seasons of this TVInformationPost.
        :type seasons: str
        """

        self._seasons = seasons

    @property
    def show_image(self):
        """Gets the show_image of this TVInformationPost.


        :return: The show_image of this TVInformationPost.
        :rtype: str
        """
        return self._show_image

    @show_image.setter
    def show_image(self, show_image):
        """Sets the show_image of this TVInformationPost.


        :param show_image: The show_image of this TVInformationPost.
        :type show_image: str
        """

        self._show_image = show_image

    @property
    def show_status(self):
        """Gets the show_status of this TVInformationPost.


        :return: The show_status of this TVInformationPost.
        :rtype: str
        """
        return self._show_status

    @show_status.setter
    def show_status(self, show_status):
        """Sets the show_status of this TVInformationPost.


        :param show_status: The show_status of this TVInformationPost.
        :type show_status: str
        """

        self._show_status = show_status

    @property
    def synopsis(self):
        """Gets the synopsis of this TVInformationPost.


        :return: The synopsis of this TVInformationPost.
        :rtype: str
        """
        return self._synopsis

    @synopsis.setter
    def synopsis(self, synopsis):
        """Sets the synopsis of this TVInformationPost.


        :param synopsis: The synopsis of this TVInformationPost.
        :type synopsis: str
        """

        self._synopsis = synopsis

    @property
    def title(self):
        """Gets the title of this TVInformationPost.


        :return: The title of this TVInformationPost.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TVInformationPost.


        :param title: The title of this TVInformationPost.
        :type title: str
        """

        self._title = title
