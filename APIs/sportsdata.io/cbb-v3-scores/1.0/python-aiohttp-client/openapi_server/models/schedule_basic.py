# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ScheduleBasic(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, away_team: str=None, away_team_id: int=None, away_team_score: int=None, away_team_seed: int=None, bracket: str=None, date_time: str=None, date_time_utc: str=None, day: str=None, game_end_date_time: str=None, game_id: int=None, global_game_id: int=None, home_team: str=None, home_team_id: int=None, home_team_score: int=None, home_team_seed: int=None, is_closed: bool=None, neutral_venue: bool=None, round: int=None, season: int=None, season_type: int=None, status: str=None, tournament_id: int=None, updated: str=None):
        """ScheduleBasic - a model defined in OpenAPI

        :param away_team: The away_team of this ScheduleBasic.
        :param away_team_id: The away_team_id of this ScheduleBasic.
        :param away_team_score: The away_team_score of this ScheduleBasic.
        :param away_team_seed: The away_team_seed of this ScheduleBasic.
        :param bracket: The bracket of this ScheduleBasic.
        :param date_time: The date_time of this ScheduleBasic.
        :param date_time_utc: The date_time_utc of this ScheduleBasic.
        :param day: The day of this ScheduleBasic.
        :param game_end_date_time: The game_end_date_time of this ScheduleBasic.
        :param game_id: The game_id of this ScheduleBasic.
        :param global_game_id: The global_game_id of this ScheduleBasic.
        :param home_team: The home_team of this ScheduleBasic.
        :param home_team_id: The home_team_id of this ScheduleBasic.
        :param home_team_score: The home_team_score of this ScheduleBasic.
        :param home_team_seed: The home_team_seed of this ScheduleBasic.
        :param is_closed: The is_closed of this ScheduleBasic.
        :param neutral_venue: The neutral_venue of this ScheduleBasic.
        :param round: The round of this ScheduleBasic.
        :param season: The season of this ScheduleBasic.
        :param season_type: The season_type of this ScheduleBasic.
        :param status: The status of this ScheduleBasic.
        :param tournament_id: The tournament_id of this ScheduleBasic.
        :param updated: The updated of this ScheduleBasic.
        """
        self.openapi_types = {
            'away_team': str,
            'away_team_id': int,
            'away_team_score': int,
            'away_team_seed': int,
            'bracket': str,
            'date_time': str,
            'date_time_utc': str,
            'day': str,
            'game_end_date_time': str,
            'game_id': int,
            'global_game_id': int,
            'home_team': str,
            'home_team_id': int,
            'home_team_score': int,
            'home_team_seed': int,
            'is_closed': bool,
            'neutral_venue': bool,
            'round': int,
            'season': int,
            'season_type': int,
            'status': str,
            'tournament_id': int,
            'updated': str
        }

        self.attribute_map = {
            'away_team': 'AwayTeam',
            'away_team_id': 'AwayTeamID',
            'away_team_score': 'AwayTeamScore',
            'away_team_seed': 'AwayTeamSeed',
            'bracket': 'Bracket',
            'date_time': 'DateTime',
            'date_time_utc': 'DateTimeUTC',
            'day': 'Day',
            'game_end_date_time': 'GameEndDateTime',
            'game_id': 'GameID',
            'global_game_id': 'GlobalGameID',
            'home_team': 'HomeTeam',
            'home_team_id': 'HomeTeamID',
            'home_team_score': 'HomeTeamScore',
            'home_team_seed': 'HomeTeamSeed',
            'is_closed': 'IsClosed',
            'neutral_venue': 'NeutralVenue',
            'round': 'Round',
            'season': 'Season',
            'season_type': 'SeasonType',
            'status': 'Status',
            'tournament_id': 'TournamentID',
            'updated': 'Updated'
        }

        self._away_team = away_team
        self._away_team_id = away_team_id
        self._away_team_score = away_team_score
        self._away_team_seed = away_team_seed
        self._bracket = bracket
        self._date_time = date_time
        self._date_time_utc = date_time_utc
        self._day = day
        self._game_end_date_time = game_end_date_time
        self._game_id = game_id
        self._global_game_id = global_game_id
        self._home_team = home_team
        self._home_team_id = home_team_id
        self._home_team_score = home_team_score
        self._home_team_seed = home_team_seed
        self._is_closed = is_closed
        self._neutral_venue = neutral_venue
        self._round = round
        self._season = season
        self._season_type = season_type
        self._status = status
        self._tournament_id = tournament_id
        self._updated = updated

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ScheduleBasic':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ScheduleBasic of this ScheduleBasic.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def away_team(self):
        """Gets the away_team of this ScheduleBasic.


        :return: The away_team of this ScheduleBasic.
        :rtype: str
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        """Sets the away_team of this ScheduleBasic.


        :param away_team: The away_team of this ScheduleBasic.
        :type away_team: str
        """

        self._away_team = away_team

    @property
    def away_team_id(self):
        """Gets the away_team_id of this ScheduleBasic.


        :return: The away_team_id of this ScheduleBasic.
        :rtype: int
        """
        return self._away_team_id

    @away_team_id.setter
    def away_team_id(self, away_team_id):
        """Sets the away_team_id of this ScheduleBasic.


        :param away_team_id: The away_team_id of this ScheduleBasic.
        :type away_team_id: int
        """

        self._away_team_id = away_team_id

    @property
    def away_team_score(self):
        """Gets the away_team_score of this ScheduleBasic.


        :return: The away_team_score of this ScheduleBasic.
        :rtype: int
        """
        return self._away_team_score

    @away_team_score.setter
    def away_team_score(self, away_team_score):
        """Sets the away_team_score of this ScheduleBasic.


        :param away_team_score: The away_team_score of this ScheduleBasic.
        :type away_team_score: int
        """

        self._away_team_score = away_team_score

    @property
    def away_team_seed(self):
        """Gets the away_team_seed of this ScheduleBasic.


        :return: The away_team_seed of this ScheduleBasic.
        :rtype: int
        """
        return self._away_team_seed

    @away_team_seed.setter
    def away_team_seed(self, away_team_seed):
        """Sets the away_team_seed of this ScheduleBasic.


        :param away_team_seed: The away_team_seed of this ScheduleBasic.
        :type away_team_seed: int
        """

        self._away_team_seed = away_team_seed

    @property
    def bracket(self):
        """Gets the bracket of this ScheduleBasic.


        :return: The bracket of this ScheduleBasic.
        :rtype: str
        """
        return self._bracket

    @bracket.setter
    def bracket(self, bracket):
        """Sets the bracket of this ScheduleBasic.


        :param bracket: The bracket of this ScheduleBasic.
        :type bracket: str
        """

        self._bracket = bracket

    @property
    def date_time(self):
        """Gets the date_time of this ScheduleBasic.


        :return: The date_time of this ScheduleBasic.
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this ScheduleBasic.


        :param date_time: The date_time of this ScheduleBasic.
        :type date_time: str
        """

        self._date_time = date_time

    @property
    def date_time_utc(self):
        """Gets the date_time_utc of this ScheduleBasic.


        :return: The date_time_utc of this ScheduleBasic.
        :rtype: str
        """
        return self._date_time_utc

    @date_time_utc.setter
    def date_time_utc(self, date_time_utc):
        """Sets the date_time_utc of this ScheduleBasic.


        :param date_time_utc: The date_time_utc of this ScheduleBasic.
        :type date_time_utc: str
        """

        self._date_time_utc = date_time_utc

    @property
    def day(self):
        """Gets the day of this ScheduleBasic.


        :return: The day of this ScheduleBasic.
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this ScheduleBasic.


        :param day: The day of this ScheduleBasic.
        :type day: str
        """

        self._day = day

    @property
    def game_end_date_time(self):
        """Gets the game_end_date_time of this ScheduleBasic.


        :return: The game_end_date_time of this ScheduleBasic.
        :rtype: str
        """
        return self._game_end_date_time

    @game_end_date_time.setter
    def game_end_date_time(self, game_end_date_time):
        """Sets the game_end_date_time of this ScheduleBasic.


        :param game_end_date_time: The game_end_date_time of this ScheduleBasic.
        :type game_end_date_time: str
        """

        self._game_end_date_time = game_end_date_time

    @property
    def game_id(self):
        """Gets the game_id of this ScheduleBasic.


        :return: The game_id of this ScheduleBasic.
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this ScheduleBasic.


        :param game_id: The game_id of this ScheduleBasic.
        :type game_id: int
        """

        self._game_id = game_id

    @property
    def global_game_id(self):
        """Gets the global_game_id of this ScheduleBasic.


        :return: The global_game_id of this ScheduleBasic.
        :rtype: int
        """
        return self._global_game_id

    @global_game_id.setter
    def global_game_id(self, global_game_id):
        """Sets the global_game_id of this ScheduleBasic.


        :param global_game_id: The global_game_id of this ScheduleBasic.
        :type global_game_id: int
        """

        self._global_game_id = global_game_id

    @property
    def home_team(self):
        """Gets the home_team of this ScheduleBasic.


        :return: The home_team of this ScheduleBasic.
        :rtype: str
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        """Sets the home_team of this ScheduleBasic.


        :param home_team: The home_team of this ScheduleBasic.
        :type home_team: str
        """

        self._home_team = home_team

    @property
    def home_team_id(self):
        """Gets the home_team_id of this ScheduleBasic.


        :return: The home_team_id of this ScheduleBasic.
        :rtype: int
        """
        return self._home_team_id

    @home_team_id.setter
    def home_team_id(self, home_team_id):
        """Sets the home_team_id of this ScheduleBasic.


        :param home_team_id: The home_team_id of this ScheduleBasic.
        :type home_team_id: int
        """

        self._home_team_id = home_team_id

    @property
    def home_team_score(self):
        """Gets the home_team_score of this ScheduleBasic.


        :return: The home_team_score of this ScheduleBasic.
        :rtype: int
        """
        return self._home_team_score

    @home_team_score.setter
    def home_team_score(self, home_team_score):
        """Sets the home_team_score of this ScheduleBasic.


        :param home_team_score: The home_team_score of this ScheduleBasic.
        :type home_team_score: int
        """

        self._home_team_score = home_team_score

    @property
    def home_team_seed(self):
        """Gets the home_team_seed of this ScheduleBasic.


        :return: The home_team_seed of this ScheduleBasic.
        :rtype: int
        """
        return self._home_team_seed

    @home_team_seed.setter
    def home_team_seed(self, home_team_seed):
        """Sets the home_team_seed of this ScheduleBasic.


        :param home_team_seed: The home_team_seed of this ScheduleBasic.
        :type home_team_seed: int
        """

        self._home_team_seed = home_team_seed

    @property
    def is_closed(self):
        """Gets the is_closed of this ScheduleBasic.


        :return: The is_closed of this ScheduleBasic.
        :rtype: bool
        """
        return self._is_closed

    @is_closed.setter
    def is_closed(self, is_closed):
        """Sets the is_closed of this ScheduleBasic.


        :param is_closed: The is_closed of this ScheduleBasic.
        :type is_closed: bool
        """

        self._is_closed = is_closed

    @property
    def neutral_venue(self):
        """Gets the neutral_venue of this ScheduleBasic.


        :return: The neutral_venue of this ScheduleBasic.
        :rtype: bool
        """
        return self._neutral_venue

    @neutral_venue.setter
    def neutral_venue(self, neutral_venue):
        """Sets the neutral_venue of this ScheduleBasic.


        :param neutral_venue: The neutral_venue of this ScheduleBasic.
        :type neutral_venue: bool
        """

        self._neutral_venue = neutral_venue

    @property
    def round(self):
        """Gets the round of this ScheduleBasic.


        :return: The round of this ScheduleBasic.
        :rtype: int
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this ScheduleBasic.


        :param round: The round of this ScheduleBasic.
        :type round: int
        """

        self._round = round

    @property
    def season(self):
        """Gets the season of this ScheduleBasic.


        :return: The season of this ScheduleBasic.
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this ScheduleBasic.


        :param season: The season of this ScheduleBasic.
        :type season: int
        """

        self._season = season

    @property
    def season_type(self):
        """Gets the season_type of this ScheduleBasic.


        :return: The season_type of this ScheduleBasic.
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this ScheduleBasic.


        :param season_type: The season_type of this ScheduleBasic.
        :type season_type: int
        """

        self._season_type = season_type

    @property
    def status(self):
        """Gets the status of this ScheduleBasic.


        :return: The status of this ScheduleBasic.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScheduleBasic.


        :param status: The status of this ScheduleBasic.
        :type status: str
        """

        self._status = status

    @property
    def tournament_id(self):
        """Gets the tournament_id of this ScheduleBasic.


        :return: The tournament_id of this ScheduleBasic.
        :rtype: int
        """
        return self._tournament_id

    @tournament_id.setter
    def tournament_id(self, tournament_id):
        """Sets the tournament_id of this ScheduleBasic.


        :param tournament_id: The tournament_id of this ScheduleBasic.
        :type tournament_id: int
        """

        self._tournament_id = tournament_id

    @property
    def updated(self):
        """Gets the updated of this ScheduleBasic.


        :return: The updated of this ScheduleBasic.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ScheduleBasic.


        :param updated: The updated of this ScheduleBasic.
        :type updated: str
        """

        self._updated = updated
