# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.goaltender import Goaltender
from openapi_server import util


class StartingGoaltenders(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, away_goaltender: Goaltender=None, away_team: str=None, away_team_id: int=None, date_time: str=None, day: str=None, game_id: int=None, home_goaltender: Goaltender=None, home_team: str=None, home_team_id: int=None, season: int=None, season_type: int=None, status: str=None):
        """StartingGoaltenders - a model defined in OpenAPI

        :param away_goaltender: The away_goaltender of this StartingGoaltenders.
        :param away_team: The away_team of this StartingGoaltenders.
        :param away_team_id: The away_team_id of this StartingGoaltenders.
        :param date_time: The date_time of this StartingGoaltenders.
        :param day: The day of this StartingGoaltenders.
        :param game_id: The game_id of this StartingGoaltenders.
        :param home_goaltender: The home_goaltender of this StartingGoaltenders.
        :param home_team: The home_team of this StartingGoaltenders.
        :param home_team_id: The home_team_id of this StartingGoaltenders.
        :param season: The season of this StartingGoaltenders.
        :param season_type: The season_type of this StartingGoaltenders.
        :param status: The status of this StartingGoaltenders.
        """
        self.openapi_types = {
            'away_goaltender': Goaltender,
            'away_team': str,
            'away_team_id': int,
            'date_time': str,
            'day': str,
            'game_id': int,
            'home_goaltender': Goaltender,
            'home_team': str,
            'home_team_id': int,
            'season': int,
            'season_type': int,
            'status': str
        }

        self.attribute_map = {
            'away_goaltender': 'AwayGoaltender',
            'away_team': 'AwayTeam',
            'away_team_id': 'AwayTeamID',
            'date_time': 'DateTime',
            'day': 'Day',
            'game_id': 'GameID',
            'home_goaltender': 'HomeGoaltender',
            'home_team': 'HomeTeam',
            'home_team_id': 'HomeTeamID',
            'season': 'Season',
            'season_type': 'SeasonType',
            'status': 'Status'
        }

        self._away_goaltender = away_goaltender
        self._away_team = away_team
        self._away_team_id = away_team_id
        self._date_time = date_time
        self._day = day
        self._game_id = game_id
        self._home_goaltender = home_goaltender
        self._home_team = home_team
        self._home_team_id = home_team_id
        self._season = season
        self._season_type = season_type
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'StartingGoaltenders':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The StartingGoaltenders of this StartingGoaltenders.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def away_goaltender(self):
        """Gets the away_goaltender of this StartingGoaltenders.


        :return: The away_goaltender of this StartingGoaltenders.
        :rtype: Goaltender
        """
        return self._away_goaltender

    @away_goaltender.setter
    def away_goaltender(self, away_goaltender):
        """Sets the away_goaltender of this StartingGoaltenders.


        :param away_goaltender: The away_goaltender of this StartingGoaltenders.
        :type away_goaltender: Goaltender
        """

        self._away_goaltender = away_goaltender

    @property
    def away_team(self):
        """Gets the away_team of this StartingGoaltenders.


        :return: The away_team of this StartingGoaltenders.
        :rtype: str
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        """Sets the away_team of this StartingGoaltenders.


        :param away_team: The away_team of this StartingGoaltenders.
        :type away_team: str
        """

        self._away_team = away_team

    @property
    def away_team_id(self):
        """Gets the away_team_id of this StartingGoaltenders.


        :return: The away_team_id of this StartingGoaltenders.
        :rtype: int
        """
        return self._away_team_id

    @away_team_id.setter
    def away_team_id(self, away_team_id):
        """Sets the away_team_id of this StartingGoaltenders.


        :param away_team_id: The away_team_id of this StartingGoaltenders.
        :type away_team_id: int
        """

        self._away_team_id = away_team_id

    @property
    def date_time(self):
        """Gets the date_time of this StartingGoaltenders.


        :return: The date_time of this StartingGoaltenders.
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this StartingGoaltenders.


        :param date_time: The date_time of this StartingGoaltenders.
        :type date_time: str
        """

        self._date_time = date_time

    @property
    def day(self):
        """Gets the day of this StartingGoaltenders.


        :return: The day of this StartingGoaltenders.
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this StartingGoaltenders.


        :param day: The day of this StartingGoaltenders.
        :type day: str
        """

        self._day = day

    @property
    def game_id(self):
        """Gets the game_id of this StartingGoaltenders.


        :return: The game_id of this StartingGoaltenders.
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this StartingGoaltenders.


        :param game_id: The game_id of this StartingGoaltenders.
        :type game_id: int
        """

        self._game_id = game_id

    @property
    def home_goaltender(self):
        """Gets the home_goaltender of this StartingGoaltenders.


        :return: The home_goaltender of this StartingGoaltenders.
        :rtype: Goaltender
        """
        return self._home_goaltender

    @home_goaltender.setter
    def home_goaltender(self, home_goaltender):
        """Sets the home_goaltender of this StartingGoaltenders.


        :param home_goaltender: The home_goaltender of this StartingGoaltenders.
        :type home_goaltender: Goaltender
        """

        self._home_goaltender = home_goaltender

    @property
    def home_team(self):
        """Gets the home_team of this StartingGoaltenders.


        :return: The home_team of this StartingGoaltenders.
        :rtype: str
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        """Sets the home_team of this StartingGoaltenders.


        :param home_team: The home_team of this StartingGoaltenders.
        :type home_team: str
        """

        self._home_team = home_team

    @property
    def home_team_id(self):
        """Gets the home_team_id of this StartingGoaltenders.


        :return: The home_team_id of this StartingGoaltenders.
        :rtype: int
        """
        return self._home_team_id

    @home_team_id.setter
    def home_team_id(self, home_team_id):
        """Sets the home_team_id of this StartingGoaltenders.


        :param home_team_id: The home_team_id of this StartingGoaltenders.
        :type home_team_id: int
        """

        self._home_team_id = home_team_id

    @property
    def season(self):
        """Gets the season of this StartingGoaltenders.


        :return: The season of this StartingGoaltenders.
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this StartingGoaltenders.


        :param season: The season of this StartingGoaltenders.
        :type season: int
        """

        self._season = season

    @property
    def season_type(self):
        """Gets the season_type of this StartingGoaltenders.


        :return: The season_type of this StartingGoaltenders.
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this StartingGoaltenders.


        :param season_type: The season_type of this StartingGoaltenders.
        :type season_type: int
        """

        self._season_type = season_type

    @property
    def status(self):
        """Gets the status of this StartingGoaltenders.


        :return: The status of this StartingGoaltenders.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StartingGoaltenders.


        :param status: The status of this StartingGoaltenders.
        :type status: str
        """

        self._status = status
