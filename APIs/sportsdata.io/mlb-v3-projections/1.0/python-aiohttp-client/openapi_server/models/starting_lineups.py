# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.lineup import Lineup
from openapi_server import util


class StartingLineups(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, away_batting_lineup: List[Lineup]=None, away_starting_pitcher: Lineup=None, away_team: str=None, away_team_id: int=None, date_time: str=None, day: str=None, game_id: int=None, home_batting_lineup: List[Lineup]=None, home_starting_pitcher: Lineup=None, home_team: str=None, home_team_id: int=None, season: int=None, season_type: int=None, status: str=None):
        """StartingLineups - a model defined in OpenAPI

        :param away_batting_lineup: The away_batting_lineup of this StartingLineups.
        :param away_starting_pitcher: The away_starting_pitcher of this StartingLineups.
        :param away_team: The away_team of this StartingLineups.
        :param away_team_id: The away_team_id of this StartingLineups.
        :param date_time: The date_time of this StartingLineups.
        :param day: The day of this StartingLineups.
        :param game_id: The game_id of this StartingLineups.
        :param home_batting_lineup: The home_batting_lineup of this StartingLineups.
        :param home_starting_pitcher: The home_starting_pitcher of this StartingLineups.
        :param home_team: The home_team of this StartingLineups.
        :param home_team_id: The home_team_id of this StartingLineups.
        :param season: The season of this StartingLineups.
        :param season_type: The season_type of this StartingLineups.
        :param status: The status of this StartingLineups.
        """
        self.openapi_types = {
            'away_batting_lineup': List[Lineup],
            'away_starting_pitcher': Lineup,
            'away_team': str,
            'away_team_id': int,
            'date_time': str,
            'day': str,
            'game_id': int,
            'home_batting_lineup': List[Lineup],
            'home_starting_pitcher': Lineup,
            'home_team': str,
            'home_team_id': int,
            'season': int,
            'season_type': int,
            'status': str
        }

        self.attribute_map = {
            'away_batting_lineup': 'AwayBattingLineup',
            'away_starting_pitcher': 'AwayStartingPitcher',
            'away_team': 'AwayTeam',
            'away_team_id': 'AwayTeamID',
            'date_time': 'DateTime',
            'day': 'Day',
            'game_id': 'GameID',
            'home_batting_lineup': 'HomeBattingLineup',
            'home_starting_pitcher': 'HomeStartingPitcher',
            'home_team': 'HomeTeam',
            'home_team_id': 'HomeTeamID',
            'season': 'Season',
            'season_type': 'SeasonType',
            'status': 'Status'
        }

        self._away_batting_lineup = away_batting_lineup
        self._away_starting_pitcher = away_starting_pitcher
        self._away_team = away_team
        self._away_team_id = away_team_id
        self._date_time = date_time
        self._day = day
        self._game_id = game_id
        self._home_batting_lineup = home_batting_lineup
        self._home_starting_pitcher = home_starting_pitcher
        self._home_team = home_team
        self._home_team_id = home_team_id
        self._season = season
        self._season_type = season_type
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'StartingLineups':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The StartingLineups of this StartingLineups.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def away_batting_lineup(self):
        """Gets the away_batting_lineup of this StartingLineups.


        :return: The away_batting_lineup of this StartingLineups.
        :rtype: List[Lineup]
        """
        return self._away_batting_lineup

    @away_batting_lineup.setter
    def away_batting_lineup(self, away_batting_lineup):
        """Sets the away_batting_lineup of this StartingLineups.


        :param away_batting_lineup: The away_batting_lineup of this StartingLineups.
        :type away_batting_lineup: List[Lineup]
        """

        self._away_batting_lineup = away_batting_lineup

    @property
    def away_starting_pitcher(self):
        """Gets the away_starting_pitcher of this StartingLineups.


        :return: The away_starting_pitcher of this StartingLineups.
        :rtype: Lineup
        """
        return self._away_starting_pitcher

    @away_starting_pitcher.setter
    def away_starting_pitcher(self, away_starting_pitcher):
        """Sets the away_starting_pitcher of this StartingLineups.


        :param away_starting_pitcher: The away_starting_pitcher of this StartingLineups.
        :type away_starting_pitcher: Lineup
        """

        self._away_starting_pitcher = away_starting_pitcher

    @property
    def away_team(self):
        """Gets the away_team of this StartingLineups.


        :return: The away_team of this StartingLineups.
        :rtype: str
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        """Sets the away_team of this StartingLineups.


        :param away_team: The away_team of this StartingLineups.
        :type away_team: str
        """

        self._away_team = away_team

    @property
    def away_team_id(self):
        """Gets the away_team_id of this StartingLineups.


        :return: The away_team_id of this StartingLineups.
        :rtype: int
        """
        return self._away_team_id

    @away_team_id.setter
    def away_team_id(self, away_team_id):
        """Sets the away_team_id of this StartingLineups.


        :param away_team_id: The away_team_id of this StartingLineups.
        :type away_team_id: int
        """

        self._away_team_id = away_team_id

    @property
    def date_time(self):
        """Gets the date_time of this StartingLineups.


        :return: The date_time of this StartingLineups.
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this StartingLineups.


        :param date_time: The date_time of this StartingLineups.
        :type date_time: str
        """

        self._date_time = date_time

    @property
    def day(self):
        """Gets the day of this StartingLineups.


        :return: The day of this StartingLineups.
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this StartingLineups.


        :param day: The day of this StartingLineups.
        :type day: str
        """

        self._day = day

    @property
    def game_id(self):
        """Gets the game_id of this StartingLineups.


        :return: The game_id of this StartingLineups.
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this StartingLineups.


        :param game_id: The game_id of this StartingLineups.
        :type game_id: int
        """

        self._game_id = game_id

    @property
    def home_batting_lineup(self):
        """Gets the home_batting_lineup of this StartingLineups.


        :return: The home_batting_lineup of this StartingLineups.
        :rtype: List[Lineup]
        """
        return self._home_batting_lineup

    @home_batting_lineup.setter
    def home_batting_lineup(self, home_batting_lineup):
        """Sets the home_batting_lineup of this StartingLineups.


        :param home_batting_lineup: The home_batting_lineup of this StartingLineups.
        :type home_batting_lineup: List[Lineup]
        """

        self._home_batting_lineup = home_batting_lineup

    @property
    def home_starting_pitcher(self):
        """Gets the home_starting_pitcher of this StartingLineups.


        :return: The home_starting_pitcher of this StartingLineups.
        :rtype: Lineup
        """
        return self._home_starting_pitcher

    @home_starting_pitcher.setter
    def home_starting_pitcher(self, home_starting_pitcher):
        """Sets the home_starting_pitcher of this StartingLineups.


        :param home_starting_pitcher: The home_starting_pitcher of this StartingLineups.
        :type home_starting_pitcher: Lineup
        """

        self._home_starting_pitcher = home_starting_pitcher

    @property
    def home_team(self):
        """Gets the home_team of this StartingLineups.


        :return: The home_team of this StartingLineups.
        :rtype: str
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        """Sets the home_team of this StartingLineups.


        :param home_team: The home_team of this StartingLineups.
        :type home_team: str
        """

        self._home_team = home_team

    @property
    def home_team_id(self):
        """Gets the home_team_id of this StartingLineups.


        :return: The home_team_id of this StartingLineups.
        :rtype: int
        """
        return self._home_team_id

    @home_team_id.setter
    def home_team_id(self, home_team_id):
        """Sets the home_team_id of this StartingLineups.


        :param home_team_id: The home_team_id of this StartingLineups.
        :type home_team_id: int
        """

        self._home_team_id = home_team_id

    @property
    def season(self):
        """Gets the season of this StartingLineups.


        :return: The season of this StartingLineups.
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this StartingLineups.


        :param season: The season of this StartingLineups.
        :type season: int
        """

        self._season = season

    @property
    def season_type(self):
        """Gets the season_type of this StartingLineups.


        :return: The season_type of this StartingLineups.
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this StartingLineups.


        :param season_type: The season_type of this StartingLineups.
        :type season_type: int
        """

        self._season_type = season_type

    @property
    def status(self):
        """Gets the status of this StartingLineups.


        :return: The status of this StartingLineups.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StartingLineups.


        :param status: The status of this StartingLineups.
        :type status: str
        """

        self._status = status
