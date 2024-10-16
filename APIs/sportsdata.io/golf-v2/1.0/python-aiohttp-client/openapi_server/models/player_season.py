# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PlayerSeason(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, average_points: float=None, events: int=None, name: str=None, player_id: int=None, player_season_id: int=None, points_gained: float=None, points_lost: float=None, season: int=None, total_points: float=None, world_golf_rank: int=None, world_golf_rank_last_week: int=None):
        """PlayerSeason - a model defined in OpenAPI

        :param average_points: The average_points of this PlayerSeason.
        :param events: The events of this PlayerSeason.
        :param name: The name of this PlayerSeason.
        :param player_id: The player_id of this PlayerSeason.
        :param player_season_id: The player_season_id of this PlayerSeason.
        :param points_gained: The points_gained of this PlayerSeason.
        :param points_lost: The points_lost of this PlayerSeason.
        :param season: The season of this PlayerSeason.
        :param total_points: The total_points of this PlayerSeason.
        :param world_golf_rank: The world_golf_rank of this PlayerSeason.
        :param world_golf_rank_last_week: The world_golf_rank_last_week of this PlayerSeason.
        """
        self.openapi_types = {
            'average_points': float,
            'events': int,
            'name': str,
            'player_id': int,
            'player_season_id': int,
            'points_gained': float,
            'points_lost': float,
            'season': int,
            'total_points': float,
            'world_golf_rank': int,
            'world_golf_rank_last_week': int
        }

        self.attribute_map = {
            'average_points': 'AveragePoints',
            'events': 'Events',
            'name': 'Name',
            'player_id': 'PlayerID',
            'player_season_id': 'PlayerSeasonID',
            'points_gained': 'PointsGained',
            'points_lost': 'PointsLost',
            'season': 'Season',
            'total_points': 'TotalPoints',
            'world_golf_rank': 'WorldGolfRank',
            'world_golf_rank_last_week': 'WorldGolfRankLastWeek'
        }

        self._average_points = average_points
        self._events = events
        self._name = name
        self._player_id = player_id
        self._player_season_id = player_season_id
        self._points_gained = points_gained
        self._points_lost = points_lost
        self._season = season
        self._total_points = total_points
        self._world_golf_rank = world_golf_rank
        self._world_golf_rank_last_week = world_golf_rank_last_week

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PlayerSeason':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PlayerSeason of this PlayerSeason.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def average_points(self):
        """Gets the average_points of this PlayerSeason.


        :return: The average_points of this PlayerSeason.
        :rtype: float
        """
        return self._average_points

    @average_points.setter
    def average_points(self, average_points):
        """Sets the average_points of this PlayerSeason.


        :param average_points: The average_points of this PlayerSeason.
        :type average_points: float
        """

        self._average_points = average_points

    @property
    def events(self):
        """Gets the events of this PlayerSeason.


        :return: The events of this PlayerSeason.
        :rtype: int
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this PlayerSeason.


        :param events: The events of this PlayerSeason.
        :type events: int
        """

        self._events = events

    @property
    def name(self):
        """Gets the name of this PlayerSeason.


        :return: The name of this PlayerSeason.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerSeason.


        :param name: The name of this PlayerSeason.
        :type name: str
        """

        self._name = name

    @property
    def player_id(self):
        """Gets the player_id of this PlayerSeason.


        :return: The player_id of this PlayerSeason.
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this PlayerSeason.


        :param player_id: The player_id of this PlayerSeason.
        :type player_id: int
        """

        self._player_id = player_id

    @property
    def player_season_id(self):
        """Gets the player_season_id of this PlayerSeason.


        :return: The player_season_id of this PlayerSeason.
        :rtype: int
        """
        return self._player_season_id

    @player_season_id.setter
    def player_season_id(self, player_season_id):
        """Sets the player_season_id of this PlayerSeason.


        :param player_season_id: The player_season_id of this PlayerSeason.
        :type player_season_id: int
        """

        self._player_season_id = player_season_id

    @property
    def points_gained(self):
        """Gets the points_gained of this PlayerSeason.


        :return: The points_gained of this PlayerSeason.
        :rtype: float
        """
        return self._points_gained

    @points_gained.setter
    def points_gained(self, points_gained):
        """Sets the points_gained of this PlayerSeason.


        :param points_gained: The points_gained of this PlayerSeason.
        :type points_gained: float
        """

        self._points_gained = points_gained

    @property
    def points_lost(self):
        """Gets the points_lost of this PlayerSeason.


        :return: The points_lost of this PlayerSeason.
        :rtype: float
        """
        return self._points_lost

    @points_lost.setter
    def points_lost(self, points_lost):
        """Sets the points_lost of this PlayerSeason.


        :param points_lost: The points_lost of this PlayerSeason.
        :type points_lost: float
        """

        self._points_lost = points_lost

    @property
    def season(self):
        """Gets the season of this PlayerSeason.


        :return: The season of this PlayerSeason.
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this PlayerSeason.


        :param season: The season of this PlayerSeason.
        :type season: int
        """

        self._season = season

    @property
    def total_points(self):
        """Gets the total_points of this PlayerSeason.


        :return: The total_points of this PlayerSeason.
        :rtype: float
        """
        return self._total_points

    @total_points.setter
    def total_points(self, total_points):
        """Sets the total_points of this PlayerSeason.


        :param total_points: The total_points of this PlayerSeason.
        :type total_points: float
        """

        self._total_points = total_points

    @property
    def world_golf_rank(self):
        """Gets the world_golf_rank of this PlayerSeason.


        :return: The world_golf_rank of this PlayerSeason.
        :rtype: int
        """
        return self._world_golf_rank

    @world_golf_rank.setter
    def world_golf_rank(self, world_golf_rank):
        """Sets the world_golf_rank of this PlayerSeason.


        :param world_golf_rank: The world_golf_rank of this PlayerSeason.
        :type world_golf_rank: int
        """

        self._world_golf_rank = world_golf_rank

    @property
    def world_golf_rank_last_week(self):
        """Gets the world_golf_rank_last_week of this PlayerSeason.


        :return: The world_golf_rank_last_week of this PlayerSeason.
        :rtype: int
        """
        return self._world_golf_rank_last_week

    @world_golf_rank_last_week.setter
    def world_golf_rank_last_week(self, world_golf_rank_last_week):
        """Sets the world_golf_rank_last_week of this PlayerSeason.


        :param world_golf_rank_last_week: The world_golf_rank_last_week of this PlayerSeason.
        :type world_golf_rank_last_week: int
        """

        self._world_golf_rank_last_week = world_golf_rank_last_week
