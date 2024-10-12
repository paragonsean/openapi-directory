# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DailyFantasyScoring(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _date: str=None, fantasy_points: float=None, fantasy_points_draft_kings: float=None, fantasy_points_fan_duel: float=None, fantasy_points_fantasy_draft: float=None, fantasy_points_ppr: float=None, fantasy_points_yahoo: float=None, has_started: bool=None, is_in_progress: bool=None, is_over: bool=None, name: str=None, player_id: int=None, position: str=None, team: str=None):
        """DailyFantasyScoring - a model defined in OpenAPI

        :param _date: The _date of this DailyFantasyScoring.
        :param fantasy_points: The fantasy_points of this DailyFantasyScoring.
        :param fantasy_points_draft_kings: The fantasy_points_draft_kings of this DailyFantasyScoring.
        :param fantasy_points_fan_duel: The fantasy_points_fan_duel of this DailyFantasyScoring.
        :param fantasy_points_fantasy_draft: The fantasy_points_fantasy_draft of this DailyFantasyScoring.
        :param fantasy_points_ppr: The fantasy_points_ppr of this DailyFantasyScoring.
        :param fantasy_points_yahoo: The fantasy_points_yahoo of this DailyFantasyScoring.
        :param has_started: The has_started of this DailyFantasyScoring.
        :param is_in_progress: The is_in_progress of this DailyFantasyScoring.
        :param is_over: The is_over of this DailyFantasyScoring.
        :param name: The name of this DailyFantasyScoring.
        :param player_id: The player_id of this DailyFantasyScoring.
        :param position: The position of this DailyFantasyScoring.
        :param team: The team of this DailyFantasyScoring.
        """
        self.openapi_types = {
            '_date': str,
            'fantasy_points': float,
            'fantasy_points_draft_kings': float,
            'fantasy_points_fan_duel': float,
            'fantasy_points_fantasy_draft': float,
            'fantasy_points_ppr': float,
            'fantasy_points_yahoo': float,
            'has_started': bool,
            'is_in_progress': bool,
            'is_over': bool,
            'name': str,
            'player_id': int,
            'position': str,
            'team': str
        }

        self.attribute_map = {
            '_date': 'Date',
            'fantasy_points': 'FantasyPoints',
            'fantasy_points_draft_kings': 'FantasyPointsDraftKings',
            'fantasy_points_fan_duel': 'FantasyPointsFanDuel',
            'fantasy_points_fantasy_draft': 'FantasyPointsFantasyDraft',
            'fantasy_points_ppr': 'FantasyPointsPPR',
            'fantasy_points_yahoo': 'FantasyPointsYahoo',
            'has_started': 'HasStarted',
            'is_in_progress': 'IsInProgress',
            'is_over': 'IsOver',
            'name': 'Name',
            'player_id': 'PlayerID',
            'position': 'Position',
            'team': 'Team'
        }

        self.__date = _date
        self._fantasy_points = fantasy_points
        self._fantasy_points_draft_kings = fantasy_points_draft_kings
        self._fantasy_points_fan_duel = fantasy_points_fan_duel
        self._fantasy_points_fantasy_draft = fantasy_points_fantasy_draft
        self._fantasy_points_ppr = fantasy_points_ppr
        self._fantasy_points_yahoo = fantasy_points_yahoo
        self._has_started = has_started
        self._is_in_progress = is_in_progress
        self._is_over = is_over
        self._name = name
        self._player_id = player_id
        self._position = position
        self._team = team

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DailyFantasyScoring':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DailyFantasyScoring of this DailyFantasyScoring.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _date(self):
        """Gets the _date of this DailyFantasyScoring.


        :return: The _date of this DailyFantasyScoring.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this DailyFantasyScoring.


        :param _date: The _date of this DailyFantasyScoring.
        :type _date: str
        """

        self.__date = _date

    @property
    def fantasy_points(self):
        """Gets the fantasy_points of this DailyFantasyScoring.


        :return: The fantasy_points of this DailyFantasyScoring.
        :rtype: float
        """
        return self._fantasy_points

    @fantasy_points.setter
    def fantasy_points(self, fantasy_points):
        """Sets the fantasy_points of this DailyFantasyScoring.


        :param fantasy_points: The fantasy_points of this DailyFantasyScoring.
        :type fantasy_points: float
        """

        self._fantasy_points = fantasy_points

    @property
    def fantasy_points_draft_kings(self):
        """Gets the fantasy_points_draft_kings of this DailyFantasyScoring.


        :return: The fantasy_points_draft_kings of this DailyFantasyScoring.
        :rtype: float
        """
        return self._fantasy_points_draft_kings

    @fantasy_points_draft_kings.setter
    def fantasy_points_draft_kings(self, fantasy_points_draft_kings):
        """Sets the fantasy_points_draft_kings of this DailyFantasyScoring.


        :param fantasy_points_draft_kings: The fantasy_points_draft_kings of this DailyFantasyScoring.
        :type fantasy_points_draft_kings: float
        """

        self._fantasy_points_draft_kings = fantasy_points_draft_kings

    @property
    def fantasy_points_fan_duel(self):
        """Gets the fantasy_points_fan_duel of this DailyFantasyScoring.


        :return: The fantasy_points_fan_duel of this DailyFantasyScoring.
        :rtype: float
        """
        return self._fantasy_points_fan_duel

    @fantasy_points_fan_duel.setter
    def fantasy_points_fan_duel(self, fantasy_points_fan_duel):
        """Sets the fantasy_points_fan_duel of this DailyFantasyScoring.


        :param fantasy_points_fan_duel: The fantasy_points_fan_duel of this DailyFantasyScoring.
        :type fantasy_points_fan_duel: float
        """

        self._fantasy_points_fan_duel = fantasy_points_fan_duel

    @property
    def fantasy_points_fantasy_draft(self):
        """Gets the fantasy_points_fantasy_draft of this DailyFantasyScoring.


        :return: The fantasy_points_fantasy_draft of this DailyFantasyScoring.
        :rtype: float
        """
        return self._fantasy_points_fantasy_draft

    @fantasy_points_fantasy_draft.setter
    def fantasy_points_fantasy_draft(self, fantasy_points_fantasy_draft):
        """Sets the fantasy_points_fantasy_draft of this DailyFantasyScoring.


        :param fantasy_points_fantasy_draft: The fantasy_points_fantasy_draft of this DailyFantasyScoring.
        :type fantasy_points_fantasy_draft: float
        """

        self._fantasy_points_fantasy_draft = fantasy_points_fantasy_draft

    @property
    def fantasy_points_ppr(self):
        """Gets the fantasy_points_ppr of this DailyFantasyScoring.


        :return: The fantasy_points_ppr of this DailyFantasyScoring.
        :rtype: float
        """
        return self._fantasy_points_ppr

    @fantasy_points_ppr.setter
    def fantasy_points_ppr(self, fantasy_points_ppr):
        """Sets the fantasy_points_ppr of this DailyFantasyScoring.


        :param fantasy_points_ppr: The fantasy_points_ppr of this DailyFantasyScoring.
        :type fantasy_points_ppr: float
        """

        self._fantasy_points_ppr = fantasy_points_ppr

    @property
    def fantasy_points_yahoo(self):
        """Gets the fantasy_points_yahoo of this DailyFantasyScoring.


        :return: The fantasy_points_yahoo of this DailyFantasyScoring.
        :rtype: float
        """
        return self._fantasy_points_yahoo

    @fantasy_points_yahoo.setter
    def fantasy_points_yahoo(self, fantasy_points_yahoo):
        """Sets the fantasy_points_yahoo of this DailyFantasyScoring.


        :param fantasy_points_yahoo: The fantasy_points_yahoo of this DailyFantasyScoring.
        :type fantasy_points_yahoo: float
        """

        self._fantasy_points_yahoo = fantasy_points_yahoo

    @property
    def has_started(self):
        """Gets the has_started of this DailyFantasyScoring.


        :return: The has_started of this DailyFantasyScoring.
        :rtype: bool
        """
        return self._has_started

    @has_started.setter
    def has_started(self, has_started):
        """Sets the has_started of this DailyFantasyScoring.


        :param has_started: The has_started of this DailyFantasyScoring.
        :type has_started: bool
        """

        self._has_started = has_started

    @property
    def is_in_progress(self):
        """Gets the is_in_progress of this DailyFantasyScoring.


        :return: The is_in_progress of this DailyFantasyScoring.
        :rtype: bool
        """
        return self._is_in_progress

    @is_in_progress.setter
    def is_in_progress(self, is_in_progress):
        """Sets the is_in_progress of this DailyFantasyScoring.


        :param is_in_progress: The is_in_progress of this DailyFantasyScoring.
        :type is_in_progress: bool
        """

        self._is_in_progress = is_in_progress

    @property
    def is_over(self):
        """Gets the is_over of this DailyFantasyScoring.


        :return: The is_over of this DailyFantasyScoring.
        :rtype: bool
        """
        return self._is_over

    @is_over.setter
    def is_over(self, is_over):
        """Sets the is_over of this DailyFantasyScoring.


        :param is_over: The is_over of this DailyFantasyScoring.
        :type is_over: bool
        """

        self._is_over = is_over

    @property
    def name(self):
        """Gets the name of this DailyFantasyScoring.


        :return: The name of this DailyFantasyScoring.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DailyFantasyScoring.


        :param name: The name of this DailyFantasyScoring.
        :type name: str
        """

        self._name = name

    @property
    def player_id(self):
        """Gets the player_id of this DailyFantasyScoring.


        :return: The player_id of this DailyFantasyScoring.
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this DailyFantasyScoring.


        :param player_id: The player_id of this DailyFantasyScoring.
        :type player_id: int
        """

        self._player_id = player_id

    @property
    def position(self):
        """Gets the position of this DailyFantasyScoring.


        :return: The position of this DailyFantasyScoring.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this DailyFantasyScoring.


        :param position: The position of this DailyFantasyScoring.
        :type position: str
        """

        self._position = position

    @property
    def team(self):
        """Gets the team of this DailyFantasyScoring.


        :return: The team of this DailyFantasyScoring.
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this DailyFantasyScoring.


        :param team: The team of this DailyFantasyScoring.
        :type team: str
        """

        self._team = team
