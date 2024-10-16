# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.season import Season
from openapi_server import util


class Competition(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, area_id: int=None, area_name: str=None, competition_id: int=None, format: str=None, gender: str=None, name: str=None, player_stats_coverage: bool=None, seasons: List[Season]=None, type: str=None):
        """Competition - a model defined in OpenAPI

        :param area_id: The area_id of this Competition.
        :param area_name: The area_name of this Competition.
        :param competition_id: The competition_id of this Competition.
        :param format: The format of this Competition.
        :param gender: The gender of this Competition.
        :param name: The name of this Competition.
        :param player_stats_coverage: The player_stats_coverage of this Competition.
        :param seasons: The seasons of this Competition.
        :param type: The type of this Competition.
        """
        self.openapi_types = {
            'area_id': int,
            'area_name': str,
            'competition_id': int,
            'format': str,
            'gender': str,
            'name': str,
            'player_stats_coverage': bool,
            'seasons': List[Season],
            'type': str
        }

        self.attribute_map = {
            'area_id': 'AreaId',
            'area_name': 'AreaName',
            'competition_id': 'CompetitionId',
            'format': 'Format',
            'gender': 'Gender',
            'name': 'Name',
            'player_stats_coverage': 'PlayerStatsCoverage',
            'seasons': 'Seasons',
            'type': 'Type'
        }

        self._area_id = area_id
        self._area_name = area_name
        self._competition_id = competition_id
        self._format = format
        self._gender = gender
        self._name = name
        self._player_stats_coverage = player_stats_coverage
        self._seasons = seasons
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Competition':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Competition of this Competition.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def area_id(self):
        """Gets the area_id of this Competition.


        :return: The area_id of this Competition.
        :rtype: int
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        """Sets the area_id of this Competition.


        :param area_id: The area_id of this Competition.
        :type area_id: int
        """

        self._area_id = area_id

    @property
    def area_name(self):
        """Gets the area_name of this Competition.


        :return: The area_name of this Competition.
        :rtype: str
        """
        return self._area_name

    @area_name.setter
    def area_name(self, area_name):
        """Sets the area_name of this Competition.


        :param area_name: The area_name of this Competition.
        :type area_name: str
        """

        self._area_name = area_name

    @property
    def competition_id(self):
        """Gets the competition_id of this Competition.


        :return: The competition_id of this Competition.
        :rtype: int
        """
        return self._competition_id

    @competition_id.setter
    def competition_id(self, competition_id):
        """Sets the competition_id of this Competition.


        :param competition_id: The competition_id of this Competition.
        :type competition_id: int
        """

        self._competition_id = competition_id

    @property
    def format(self):
        """Gets the format of this Competition.


        :return: The format of this Competition.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Competition.


        :param format: The format of this Competition.
        :type format: str
        """

        self._format = format

    @property
    def gender(self):
        """Gets the gender of this Competition.


        :return: The gender of this Competition.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Competition.


        :param gender: The gender of this Competition.
        :type gender: str
        """

        self._gender = gender

    @property
    def name(self):
        """Gets the name of this Competition.


        :return: The name of this Competition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Competition.


        :param name: The name of this Competition.
        :type name: str
        """

        self._name = name

    @property
    def player_stats_coverage(self):
        """Gets the player_stats_coverage of this Competition.


        :return: The player_stats_coverage of this Competition.
        :rtype: bool
        """
        return self._player_stats_coverage

    @player_stats_coverage.setter
    def player_stats_coverage(self, player_stats_coverage):
        """Sets the player_stats_coverage of this Competition.


        :param player_stats_coverage: The player_stats_coverage of this Competition.
        :type player_stats_coverage: bool
        """

        self._player_stats_coverage = player_stats_coverage

    @property
    def seasons(self):
        """Gets the seasons of this Competition.


        :return: The seasons of this Competition.
        :rtype: List[Season]
        """
        return self._seasons

    @seasons.setter
    def seasons(self, seasons):
        """Sets the seasons of this Competition.


        :param seasons: The seasons of this Competition.
        :type seasons: List[Season]
        """

        self._seasons = seasons

    @property
    def type(self):
        """Gets the type of this Competition.


        :return: The type of this Competition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Competition.


        :param type: The type of this Competition.
        :type type: str
        """

        self._type = type
