# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Inning(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, away_team_runs: int=None, game_id: int=None, home_team_runs: int=None, inning_id: int=None, inning_number: int=None):
        """Inning - a model defined in OpenAPI

        :param away_team_runs: The away_team_runs of this Inning.
        :param game_id: The game_id of this Inning.
        :param home_team_runs: The home_team_runs of this Inning.
        :param inning_id: The inning_id of this Inning.
        :param inning_number: The inning_number of this Inning.
        """
        self.openapi_types = {
            'away_team_runs': int,
            'game_id': int,
            'home_team_runs': int,
            'inning_id': int,
            'inning_number': int
        }

        self.attribute_map = {
            'away_team_runs': 'AwayTeamRuns',
            'game_id': 'GameID',
            'home_team_runs': 'HomeTeamRuns',
            'inning_id': 'InningID',
            'inning_number': 'InningNumber'
        }

        self._away_team_runs = away_team_runs
        self._game_id = game_id
        self._home_team_runs = home_team_runs
        self._inning_id = inning_id
        self._inning_number = inning_number

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Inning':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Inning of this Inning.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def away_team_runs(self):
        """Gets the away_team_runs of this Inning.


        :return: The away_team_runs of this Inning.
        :rtype: int
        """
        return self._away_team_runs

    @away_team_runs.setter
    def away_team_runs(self, away_team_runs):
        """Sets the away_team_runs of this Inning.


        :param away_team_runs: The away_team_runs of this Inning.
        :type away_team_runs: int
        """

        self._away_team_runs = away_team_runs

    @property
    def game_id(self):
        """Gets the game_id of this Inning.


        :return: The game_id of this Inning.
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this Inning.


        :param game_id: The game_id of this Inning.
        :type game_id: int
        """

        self._game_id = game_id

    @property
    def home_team_runs(self):
        """Gets the home_team_runs of this Inning.


        :return: The home_team_runs of this Inning.
        :rtype: int
        """
        return self._home_team_runs

    @home_team_runs.setter
    def home_team_runs(self, home_team_runs):
        """Sets the home_team_runs of this Inning.


        :param home_team_runs: The home_team_runs of this Inning.
        :type home_team_runs: int
        """

        self._home_team_runs = home_team_runs

    @property
    def inning_id(self):
        """Gets the inning_id of this Inning.


        :return: The inning_id of this Inning.
        :rtype: int
        """
        return self._inning_id

    @inning_id.setter
    def inning_id(self, inning_id):
        """Sets the inning_id of this Inning.


        :param inning_id: The inning_id of this Inning.
        :type inning_id: int
        """

        self._inning_id = inning_id

    @property
    def inning_number(self):
        """Gets the inning_number of this Inning.


        :return: The inning_number of this Inning.
        :rtype: int
        """
        return self._inning_number

    @inning_number.setter
    def inning_number(self, inning_number):
        """Sets the inning_number of this Inning.


        :param inning_number: The inning_number of this Inning.
        :type inning_number: int
        """

        self._inning_number = inning_number
