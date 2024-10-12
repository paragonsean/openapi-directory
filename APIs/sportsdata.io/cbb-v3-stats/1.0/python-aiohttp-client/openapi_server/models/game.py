# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.period import Period
from openapi_server.models.stadium import Stadium
from openapi_server import util


class Game(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attendance: int=None, away_point_spread_payout: int=None, away_rotation_number: int=None, away_team: str=None, away_team_id: int=None, away_team_money_line: int=None, away_team_previous_game_id: int=None, away_team_previous_global_game_id: int=None, away_team_score: int=None, away_team_seed: int=None, bottom_team_previous_game_id: int=None, bracket: str=None, channel: str=None, date_time: str=None, date_time_utc: str=None, day: str=None, game_end_date_time: str=None, game_id: int=None, global_away_team_id: int=None, global_game_id: int=None, global_home_team_id: int=None, home_point_spread_payout: int=None, home_rotation_number: int=None, home_team: str=None, home_team_id: int=None, home_team_money_line: int=None, home_team_previous_game_id: int=None, home_team_previous_global_game_id: int=None, home_team_score: int=None, home_team_seed: int=None, is_closed: bool=None, neutral_venue: bool=None, over_payout: int=None, over_under: float=None, period: str=None, periods: List[Period]=None, point_spread: float=None, round: int=None, season: int=None, season_type: int=None, stadium: Stadium=None, status: str=None, time_remaining_minutes: int=None, time_remaining_seconds: int=None, top_team_previous_game_id: int=None, tournament_display_order: int=None, tournament_display_order_for_home_team: str=None, tournament_id: int=None, under_payout: int=None, updated: str=None):
        """Game - a model defined in OpenAPI

        :param attendance: The attendance of this Game.
        :param away_point_spread_payout: The away_point_spread_payout of this Game.
        :param away_rotation_number: The away_rotation_number of this Game.
        :param away_team: The away_team of this Game.
        :param away_team_id: The away_team_id of this Game.
        :param away_team_money_line: The away_team_money_line of this Game.
        :param away_team_previous_game_id: The away_team_previous_game_id of this Game.
        :param away_team_previous_global_game_id: The away_team_previous_global_game_id of this Game.
        :param away_team_score: The away_team_score of this Game.
        :param away_team_seed: The away_team_seed of this Game.
        :param bottom_team_previous_game_id: The bottom_team_previous_game_id of this Game.
        :param bracket: The bracket of this Game.
        :param channel: The channel of this Game.
        :param date_time: The date_time of this Game.
        :param date_time_utc: The date_time_utc of this Game.
        :param day: The day of this Game.
        :param game_end_date_time: The game_end_date_time of this Game.
        :param game_id: The game_id of this Game.
        :param global_away_team_id: The global_away_team_id of this Game.
        :param global_game_id: The global_game_id of this Game.
        :param global_home_team_id: The global_home_team_id of this Game.
        :param home_point_spread_payout: The home_point_spread_payout of this Game.
        :param home_rotation_number: The home_rotation_number of this Game.
        :param home_team: The home_team of this Game.
        :param home_team_id: The home_team_id of this Game.
        :param home_team_money_line: The home_team_money_line of this Game.
        :param home_team_previous_game_id: The home_team_previous_game_id of this Game.
        :param home_team_previous_global_game_id: The home_team_previous_global_game_id of this Game.
        :param home_team_score: The home_team_score of this Game.
        :param home_team_seed: The home_team_seed of this Game.
        :param is_closed: The is_closed of this Game.
        :param neutral_venue: The neutral_venue of this Game.
        :param over_payout: The over_payout of this Game.
        :param over_under: The over_under of this Game.
        :param period: The period of this Game.
        :param periods: The periods of this Game.
        :param point_spread: The point_spread of this Game.
        :param round: The round of this Game.
        :param season: The season of this Game.
        :param season_type: The season_type of this Game.
        :param stadium: The stadium of this Game.
        :param status: The status of this Game.
        :param time_remaining_minutes: The time_remaining_minutes of this Game.
        :param time_remaining_seconds: The time_remaining_seconds of this Game.
        :param top_team_previous_game_id: The top_team_previous_game_id of this Game.
        :param tournament_display_order: The tournament_display_order of this Game.
        :param tournament_display_order_for_home_team: The tournament_display_order_for_home_team of this Game.
        :param tournament_id: The tournament_id of this Game.
        :param under_payout: The under_payout of this Game.
        :param updated: The updated of this Game.
        """
        self.openapi_types = {
            'attendance': int,
            'away_point_spread_payout': int,
            'away_rotation_number': int,
            'away_team': str,
            'away_team_id': int,
            'away_team_money_line': int,
            'away_team_previous_game_id': int,
            'away_team_previous_global_game_id': int,
            'away_team_score': int,
            'away_team_seed': int,
            'bottom_team_previous_game_id': int,
            'bracket': str,
            'channel': str,
            'date_time': str,
            'date_time_utc': str,
            'day': str,
            'game_end_date_time': str,
            'game_id': int,
            'global_away_team_id': int,
            'global_game_id': int,
            'global_home_team_id': int,
            'home_point_spread_payout': int,
            'home_rotation_number': int,
            'home_team': str,
            'home_team_id': int,
            'home_team_money_line': int,
            'home_team_previous_game_id': int,
            'home_team_previous_global_game_id': int,
            'home_team_score': int,
            'home_team_seed': int,
            'is_closed': bool,
            'neutral_venue': bool,
            'over_payout': int,
            'over_under': float,
            'period': str,
            'periods': List[Period],
            'point_spread': float,
            'round': int,
            'season': int,
            'season_type': int,
            'stadium': Stadium,
            'status': str,
            'time_remaining_minutes': int,
            'time_remaining_seconds': int,
            'top_team_previous_game_id': int,
            'tournament_display_order': int,
            'tournament_display_order_for_home_team': str,
            'tournament_id': int,
            'under_payout': int,
            'updated': str
        }

        self.attribute_map = {
            'attendance': 'Attendance',
            'away_point_spread_payout': 'AwayPointSpreadPayout',
            'away_rotation_number': 'AwayRotationNumber',
            'away_team': 'AwayTeam',
            'away_team_id': 'AwayTeamID',
            'away_team_money_line': 'AwayTeamMoneyLine',
            'away_team_previous_game_id': 'AwayTeamPreviousGameID',
            'away_team_previous_global_game_id': 'AwayTeamPreviousGlobalGameID',
            'away_team_score': 'AwayTeamScore',
            'away_team_seed': 'AwayTeamSeed',
            'bottom_team_previous_game_id': 'BottomTeamPreviousGameId',
            'bracket': 'Bracket',
            'channel': 'Channel',
            'date_time': 'DateTime',
            'date_time_utc': 'DateTimeUTC',
            'day': 'Day',
            'game_end_date_time': 'GameEndDateTime',
            'game_id': 'GameID',
            'global_away_team_id': 'GlobalAwayTeamID',
            'global_game_id': 'GlobalGameID',
            'global_home_team_id': 'GlobalHomeTeamID',
            'home_point_spread_payout': 'HomePointSpreadPayout',
            'home_rotation_number': 'HomeRotationNumber',
            'home_team': 'HomeTeam',
            'home_team_id': 'HomeTeamID',
            'home_team_money_line': 'HomeTeamMoneyLine',
            'home_team_previous_game_id': 'HomeTeamPreviousGameID',
            'home_team_previous_global_game_id': 'HomeTeamPreviousGlobalGameID',
            'home_team_score': 'HomeTeamScore',
            'home_team_seed': 'HomeTeamSeed',
            'is_closed': 'IsClosed',
            'neutral_venue': 'NeutralVenue',
            'over_payout': 'OverPayout',
            'over_under': 'OverUnder',
            'period': 'Period',
            'periods': 'Periods',
            'point_spread': 'PointSpread',
            'round': 'Round',
            'season': 'Season',
            'season_type': 'SeasonType',
            'stadium': 'Stadium',
            'status': 'Status',
            'time_remaining_minutes': 'TimeRemainingMinutes',
            'time_remaining_seconds': 'TimeRemainingSeconds',
            'top_team_previous_game_id': 'TopTeamPreviousGameId',
            'tournament_display_order': 'TournamentDisplayOrder',
            'tournament_display_order_for_home_team': 'TournamentDisplayOrderForHomeTeam',
            'tournament_id': 'TournamentID',
            'under_payout': 'UnderPayout',
            'updated': 'Updated'
        }

        self._attendance = attendance
        self._away_point_spread_payout = away_point_spread_payout
        self._away_rotation_number = away_rotation_number
        self._away_team = away_team
        self._away_team_id = away_team_id
        self._away_team_money_line = away_team_money_line
        self._away_team_previous_game_id = away_team_previous_game_id
        self._away_team_previous_global_game_id = away_team_previous_global_game_id
        self._away_team_score = away_team_score
        self._away_team_seed = away_team_seed
        self._bottom_team_previous_game_id = bottom_team_previous_game_id
        self._bracket = bracket
        self._channel = channel
        self._date_time = date_time
        self._date_time_utc = date_time_utc
        self._day = day
        self._game_end_date_time = game_end_date_time
        self._game_id = game_id
        self._global_away_team_id = global_away_team_id
        self._global_game_id = global_game_id
        self._global_home_team_id = global_home_team_id
        self._home_point_spread_payout = home_point_spread_payout
        self._home_rotation_number = home_rotation_number
        self._home_team = home_team
        self._home_team_id = home_team_id
        self._home_team_money_line = home_team_money_line
        self._home_team_previous_game_id = home_team_previous_game_id
        self._home_team_previous_global_game_id = home_team_previous_global_game_id
        self._home_team_score = home_team_score
        self._home_team_seed = home_team_seed
        self._is_closed = is_closed
        self._neutral_venue = neutral_venue
        self._over_payout = over_payout
        self._over_under = over_under
        self._period = period
        self._periods = periods
        self._point_spread = point_spread
        self._round = round
        self._season = season
        self._season_type = season_type
        self._stadium = stadium
        self._status = status
        self._time_remaining_minutes = time_remaining_minutes
        self._time_remaining_seconds = time_remaining_seconds
        self._top_team_previous_game_id = top_team_previous_game_id
        self._tournament_display_order = tournament_display_order
        self._tournament_display_order_for_home_team = tournament_display_order_for_home_team
        self._tournament_id = tournament_id
        self._under_payout = under_payout
        self._updated = updated

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Game':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Game of this Game.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attendance(self):
        """Gets the attendance of this Game.


        :return: The attendance of this Game.
        :rtype: int
        """
        return self._attendance

    @attendance.setter
    def attendance(self, attendance):
        """Sets the attendance of this Game.


        :param attendance: The attendance of this Game.
        :type attendance: int
        """

        self._attendance = attendance

    @property
    def away_point_spread_payout(self):
        """Gets the away_point_spread_payout of this Game.


        :return: The away_point_spread_payout of this Game.
        :rtype: int
        """
        return self._away_point_spread_payout

    @away_point_spread_payout.setter
    def away_point_spread_payout(self, away_point_spread_payout):
        """Sets the away_point_spread_payout of this Game.


        :param away_point_spread_payout: The away_point_spread_payout of this Game.
        :type away_point_spread_payout: int
        """

        self._away_point_spread_payout = away_point_spread_payout

    @property
    def away_rotation_number(self):
        """Gets the away_rotation_number of this Game.


        :return: The away_rotation_number of this Game.
        :rtype: int
        """
        return self._away_rotation_number

    @away_rotation_number.setter
    def away_rotation_number(self, away_rotation_number):
        """Sets the away_rotation_number of this Game.


        :param away_rotation_number: The away_rotation_number of this Game.
        :type away_rotation_number: int
        """

        self._away_rotation_number = away_rotation_number

    @property
    def away_team(self):
        """Gets the away_team of this Game.


        :return: The away_team of this Game.
        :rtype: str
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        """Sets the away_team of this Game.


        :param away_team: The away_team of this Game.
        :type away_team: str
        """

        self._away_team = away_team

    @property
    def away_team_id(self):
        """Gets the away_team_id of this Game.


        :return: The away_team_id of this Game.
        :rtype: int
        """
        return self._away_team_id

    @away_team_id.setter
    def away_team_id(self, away_team_id):
        """Sets the away_team_id of this Game.


        :param away_team_id: The away_team_id of this Game.
        :type away_team_id: int
        """

        self._away_team_id = away_team_id

    @property
    def away_team_money_line(self):
        """Gets the away_team_money_line of this Game.


        :return: The away_team_money_line of this Game.
        :rtype: int
        """
        return self._away_team_money_line

    @away_team_money_line.setter
    def away_team_money_line(self, away_team_money_line):
        """Sets the away_team_money_line of this Game.


        :param away_team_money_line: The away_team_money_line of this Game.
        :type away_team_money_line: int
        """

        self._away_team_money_line = away_team_money_line

    @property
    def away_team_previous_game_id(self):
        """Gets the away_team_previous_game_id of this Game.


        :return: The away_team_previous_game_id of this Game.
        :rtype: int
        """
        return self._away_team_previous_game_id

    @away_team_previous_game_id.setter
    def away_team_previous_game_id(self, away_team_previous_game_id):
        """Sets the away_team_previous_game_id of this Game.


        :param away_team_previous_game_id: The away_team_previous_game_id of this Game.
        :type away_team_previous_game_id: int
        """

        self._away_team_previous_game_id = away_team_previous_game_id

    @property
    def away_team_previous_global_game_id(self):
        """Gets the away_team_previous_global_game_id of this Game.


        :return: The away_team_previous_global_game_id of this Game.
        :rtype: int
        """
        return self._away_team_previous_global_game_id

    @away_team_previous_global_game_id.setter
    def away_team_previous_global_game_id(self, away_team_previous_global_game_id):
        """Sets the away_team_previous_global_game_id of this Game.


        :param away_team_previous_global_game_id: The away_team_previous_global_game_id of this Game.
        :type away_team_previous_global_game_id: int
        """

        self._away_team_previous_global_game_id = away_team_previous_global_game_id

    @property
    def away_team_score(self):
        """Gets the away_team_score of this Game.


        :return: The away_team_score of this Game.
        :rtype: int
        """
        return self._away_team_score

    @away_team_score.setter
    def away_team_score(self, away_team_score):
        """Sets the away_team_score of this Game.


        :param away_team_score: The away_team_score of this Game.
        :type away_team_score: int
        """

        self._away_team_score = away_team_score

    @property
    def away_team_seed(self):
        """Gets the away_team_seed of this Game.


        :return: The away_team_seed of this Game.
        :rtype: int
        """
        return self._away_team_seed

    @away_team_seed.setter
    def away_team_seed(self, away_team_seed):
        """Sets the away_team_seed of this Game.


        :param away_team_seed: The away_team_seed of this Game.
        :type away_team_seed: int
        """

        self._away_team_seed = away_team_seed

    @property
    def bottom_team_previous_game_id(self):
        """Gets the bottom_team_previous_game_id of this Game.


        :return: The bottom_team_previous_game_id of this Game.
        :rtype: int
        """
        return self._bottom_team_previous_game_id

    @bottom_team_previous_game_id.setter
    def bottom_team_previous_game_id(self, bottom_team_previous_game_id):
        """Sets the bottom_team_previous_game_id of this Game.


        :param bottom_team_previous_game_id: The bottom_team_previous_game_id of this Game.
        :type bottom_team_previous_game_id: int
        """

        self._bottom_team_previous_game_id = bottom_team_previous_game_id

    @property
    def bracket(self):
        """Gets the bracket of this Game.


        :return: The bracket of this Game.
        :rtype: str
        """
        return self._bracket

    @bracket.setter
    def bracket(self, bracket):
        """Sets the bracket of this Game.


        :param bracket: The bracket of this Game.
        :type bracket: str
        """

        self._bracket = bracket

    @property
    def channel(self):
        """Gets the channel of this Game.


        :return: The channel of this Game.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this Game.


        :param channel: The channel of this Game.
        :type channel: str
        """

        self._channel = channel

    @property
    def date_time(self):
        """Gets the date_time of this Game.


        :return: The date_time of this Game.
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this Game.


        :param date_time: The date_time of this Game.
        :type date_time: str
        """

        self._date_time = date_time

    @property
    def date_time_utc(self):
        """Gets the date_time_utc of this Game.


        :return: The date_time_utc of this Game.
        :rtype: str
        """
        return self._date_time_utc

    @date_time_utc.setter
    def date_time_utc(self, date_time_utc):
        """Sets the date_time_utc of this Game.


        :param date_time_utc: The date_time_utc of this Game.
        :type date_time_utc: str
        """

        self._date_time_utc = date_time_utc

    @property
    def day(self):
        """Gets the day of this Game.


        :return: The day of this Game.
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this Game.


        :param day: The day of this Game.
        :type day: str
        """

        self._day = day

    @property
    def game_end_date_time(self):
        """Gets the game_end_date_time of this Game.


        :return: The game_end_date_time of this Game.
        :rtype: str
        """
        return self._game_end_date_time

    @game_end_date_time.setter
    def game_end_date_time(self, game_end_date_time):
        """Sets the game_end_date_time of this Game.


        :param game_end_date_time: The game_end_date_time of this Game.
        :type game_end_date_time: str
        """

        self._game_end_date_time = game_end_date_time

    @property
    def game_id(self):
        """Gets the game_id of this Game.


        :return: The game_id of this Game.
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this Game.


        :param game_id: The game_id of this Game.
        :type game_id: int
        """

        self._game_id = game_id

    @property
    def global_away_team_id(self):
        """Gets the global_away_team_id of this Game.


        :return: The global_away_team_id of this Game.
        :rtype: int
        """
        return self._global_away_team_id

    @global_away_team_id.setter
    def global_away_team_id(self, global_away_team_id):
        """Sets the global_away_team_id of this Game.


        :param global_away_team_id: The global_away_team_id of this Game.
        :type global_away_team_id: int
        """

        self._global_away_team_id = global_away_team_id

    @property
    def global_game_id(self):
        """Gets the global_game_id of this Game.


        :return: The global_game_id of this Game.
        :rtype: int
        """
        return self._global_game_id

    @global_game_id.setter
    def global_game_id(self, global_game_id):
        """Sets the global_game_id of this Game.


        :param global_game_id: The global_game_id of this Game.
        :type global_game_id: int
        """

        self._global_game_id = global_game_id

    @property
    def global_home_team_id(self):
        """Gets the global_home_team_id of this Game.


        :return: The global_home_team_id of this Game.
        :rtype: int
        """
        return self._global_home_team_id

    @global_home_team_id.setter
    def global_home_team_id(self, global_home_team_id):
        """Sets the global_home_team_id of this Game.


        :param global_home_team_id: The global_home_team_id of this Game.
        :type global_home_team_id: int
        """

        self._global_home_team_id = global_home_team_id

    @property
    def home_point_spread_payout(self):
        """Gets the home_point_spread_payout of this Game.


        :return: The home_point_spread_payout of this Game.
        :rtype: int
        """
        return self._home_point_spread_payout

    @home_point_spread_payout.setter
    def home_point_spread_payout(self, home_point_spread_payout):
        """Sets the home_point_spread_payout of this Game.


        :param home_point_spread_payout: The home_point_spread_payout of this Game.
        :type home_point_spread_payout: int
        """

        self._home_point_spread_payout = home_point_spread_payout

    @property
    def home_rotation_number(self):
        """Gets the home_rotation_number of this Game.


        :return: The home_rotation_number of this Game.
        :rtype: int
        """
        return self._home_rotation_number

    @home_rotation_number.setter
    def home_rotation_number(self, home_rotation_number):
        """Sets the home_rotation_number of this Game.


        :param home_rotation_number: The home_rotation_number of this Game.
        :type home_rotation_number: int
        """

        self._home_rotation_number = home_rotation_number

    @property
    def home_team(self):
        """Gets the home_team of this Game.


        :return: The home_team of this Game.
        :rtype: str
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        """Sets the home_team of this Game.


        :param home_team: The home_team of this Game.
        :type home_team: str
        """

        self._home_team = home_team

    @property
    def home_team_id(self):
        """Gets the home_team_id of this Game.


        :return: The home_team_id of this Game.
        :rtype: int
        """
        return self._home_team_id

    @home_team_id.setter
    def home_team_id(self, home_team_id):
        """Sets the home_team_id of this Game.


        :param home_team_id: The home_team_id of this Game.
        :type home_team_id: int
        """

        self._home_team_id = home_team_id

    @property
    def home_team_money_line(self):
        """Gets the home_team_money_line of this Game.


        :return: The home_team_money_line of this Game.
        :rtype: int
        """
        return self._home_team_money_line

    @home_team_money_line.setter
    def home_team_money_line(self, home_team_money_line):
        """Sets the home_team_money_line of this Game.


        :param home_team_money_line: The home_team_money_line of this Game.
        :type home_team_money_line: int
        """

        self._home_team_money_line = home_team_money_line

    @property
    def home_team_previous_game_id(self):
        """Gets the home_team_previous_game_id of this Game.


        :return: The home_team_previous_game_id of this Game.
        :rtype: int
        """
        return self._home_team_previous_game_id

    @home_team_previous_game_id.setter
    def home_team_previous_game_id(self, home_team_previous_game_id):
        """Sets the home_team_previous_game_id of this Game.


        :param home_team_previous_game_id: The home_team_previous_game_id of this Game.
        :type home_team_previous_game_id: int
        """

        self._home_team_previous_game_id = home_team_previous_game_id

    @property
    def home_team_previous_global_game_id(self):
        """Gets the home_team_previous_global_game_id of this Game.


        :return: The home_team_previous_global_game_id of this Game.
        :rtype: int
        """
        return self._home_team_previous_global_game_id

    @home_team_previous_global_game_id.setter
    def home_team_previous_global_game_id(self, home_team_previous_global_game_id):
        """Sets the home_team_previous_global_game_id of this Game.


        :param home_team_previous_global_game_id: The home_team_previous_global_game_id of this Game.
        :type home_team_previous_global_game_id: int
        """

        self._home_team_previous_global_game_id = home_team_previous_global_game_id

    @property
    def home_team_score(self):
        """Gets the home_team_score of this Game.


        :return: The home_team_score of this Game.
        :rtype: int
        """
        return self._home_team_score

    @home_team_score.setter
    def home_team_score(self, home_team_score):
        """Sets the home_team_score of this Game.


        :param home_team_score: The home_team_score of this Game.
        :type home_team_score: int
        """

        self._home_team_score = home_team_score

    @property
    def home_team_seed(self):
        """Gets the home_team_seed of this Game.


        :return: The home_team_seed of this Game.
        :rtype: int
        """
        return self._home_team_seed

    @home_team_seed.setter
    def home_team_seed(self, home_team_seed):
        """Sets the home_team_seed of this Game.


        :param home_team_seed: The home_team_seed of this Game.
        :type home_team_seed: int
        """

        self._home_team_seed = home_team_seed

    @property
    def is_closed(self):
        """Gets the is_closed of this Game.


        :return: The is_closed of this Game.
        :rtype: bool
        """
        return self._is_closed

    @is_closed.setter
    def is_closed(self, is_closed):
        """Sets the is_closed of this Game.


        :param is_closed: The is_closed of this Game.
        :type is_closed: bool
        """

        self._is_closed = is_closed

    @property
    def neutral_venue(self):
        """Gets the neutral_venue of this Game.


        :return: The neutral_venue of this Game.
        :rtype: bool
        """
        return self._neutral_venue

    @neutral_venue.setter
    def neutral_venue(self, neutral_venue):
        """Sets the neutral_venue of this Game.


        :param neutral_venue: The neutral_venue of this Game.
        :type neutral_venue: bool
        """

        self._neutral_venue = neutral_venue

    @property
    def over_payout(self):
        """Gets the over_payout of this Game.


        :return: The over_payout of this Game.
        :rtype: int
        """
        return self._over_payout

    @over_payout.setter
    def over_payout(self, over_payout):
        """Sets the over_payout of this Game.


        :param over_payout: The over_payout of this Game.
        :type over_payout: int
        """

        self._over_payout = over_payout

    @property
    def over_under(self):
        """Gets the over_under of this Game.


        :return: The over_under of this Game.
        :rtype: float
        """
        return self._over_under

    @over_under.setter
    def over_under(self, over_under):
        """Sets the over_under of this Game.


        :param over_under: The over_under of this Game.
        :type over_under: float
        """

        self._over_under = over_under

    @property
    def period(self):
        """Gets the period of this Game.


        :return: The period of this Game.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Game.


        :param period: The period of this Game.
        :type period: str
        """

        self._period = period

    @property
    def periods(self):
        """Gets the periods of this Game.


        :return: The periods of this Game.
        :rtype: List[Period]
        """
        return self._periods

    @periods.setter
    def periods(self, periods):
        """Sets the periods of this Game.


        :param periods: The periods of this Game.
        :type periods: List[Period]
        """

        self._periods = periods

    @property
    def point_spread(self):
        """Gets the point_spread of this Game.


        :return: The point_spread of this Game.
        :rtype: float
        """
        return self._point_spread

    @point_spread.setter
    def point_spread(self, point_spread):
        """Sets the point_spread of this Game.


        :param point_spread: The point_spread of this Game.
        :type point_spread: float
        """

        self._point_spread = point_spread

    @property
    def round(self):
        """Gets the round of this Game.


        :return: The round of this Game.
        :rtype: int
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this Game.


        :param round: The round of this Game.
        :type round: int
        """

        self._round = round

    @property
    def season(self):
        """Gets the season of this Game.


        :return: The season of this Game.
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this Game.


        :param season: The season of this Game.
        :type season: int
        """

        self._season = season

    @property
    def season_type(self):
        """Gets the season_type of this Game.


        :return: The season_type of this Game.
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this Game.


        :param season_type: The season_type of this Game.
        :type season_type: int
        """

        self._season_type = season_type

    @property
    def stadium(self):
        """Gets the stadium of this Game.


        :return: The stadium of this Game.
        :rtype: Stadium
        """
        return self._stadium

    @stadium.setter
    def stadium(self, stadium):
        """Sets the stadium of this Game.


        :param stadium: The stadium of this Game.
        :type stadium: Stadium
        """

        self._stadium = stadium

    @property
    def status(self):
        """Gets the status of this Game.


        :return: The status of this Game.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Game.


        :param status: The status of this Game.
        :type status: str
        """

        self._status = status

    @property
    def time_remaining_minutes(self):
        """Gets the time_remaining_minutes of this Game.


        :return: The time_remaining_minutes of this Game.
        :rtype: int
        """
        return self._time_remaining_minutes

    @time_remaining_minutes.setter
    def time_remaining_minutes(self, time_remaining_minutes):
        """Sets the time_remaining_minutes of this Game.


        :param time_remaining_minutes: The time_remaining_minutes of this Game.
        :type time_remaining_minutes: int
        """

        self._time_remaining_minutes = time_remaining_minutes

    @property
    def time_remaining_seconds(self):
        """Gets the time_remaining_seconds of this Game.


        :return: The time_remaining_seconds of this Game.
        :rtype: int
        """
        return self._time_remaining_seconds

    @time_remaining_seconds.setter
    def time_remaining_seconds(self, time_remaining_seconds):
        """Sets the time_remaining_seconds of this Game.


        :param time_remaining_seconds: The time_remaining_seconds of this Game.
        :type time_remaining_seconds: int
        """

        self._time_remaining_seconds = time_remaining_seconds

    @property
    def top_team_previous_game_id(self):
        """Gets the top_team_previous_game_id of this Game.


        :return: The top_team_previous_game_id of this Game.
        :rtype: int
        """
        return self._top_team_previous_game_id

    @top_team_previous_game_id.setter
    def top_team_previous_game_id(self, top_team_previous_game_id):
        """Sets the top_team_previous_game_id of this Game.


        :param top_team_previous_game_id: The top_team_previous_game_id of this Game.
        :type top_team_previous_game_id: int
        """

        self._top_team_previous_game_id = top_team_previous_game_id

    @property
    def tournament_display_order(self):
        """Gets the tournament_display_order of this Game.


        :return: The tournament_display_order of this Game.
        :rtype: int
        """
        return self._tournament_display_order

    @tournament_display_order.setter
    def tournament_display_order(self, tournament_display_order):
        """Sets the tournament_display_order of this Game.


        :param tournament_display_order: The tournament_display_order of this Game.
        :type tournament_display_order: int
        """

        self._tournament_display_order = tournament_display_order

    @property
    def tournament_display_order_for_home_team(self):
        """Gets the tournament_display_order_for_home_team of this Game.


        :return: The tournament_display_order_for_home_team of this Game.
        :rtype: str
        """
        return self._tournament_display_order_for_home_team

    @tournament_display_order_for_home_team.setter
    def tournament_display_order_for_home_team(self, tournament_display_order_for_home_team):
        """Sets the tournament_display_order_for_home_team of this Game.


        :param tournament_display_order_for_home_team: The tournament_display_order_for_home_team of this Game.
        :type tournament_display_order_for_home_team: str
        """

        self._tournament_display_order_for_home_team = tournament_display_order_for_home_team

    @property
    def tournament_id(self):
        """Gets the tournament_id of this Game.


        :return: The tournament_id of this Game.
        :rtype: int
        """
        return self._tournament_id

    @tournament_id.setter
    def tournament_id(self, tournament_id):
        """Sets the tournament_id of this Game.


        :param tournament_id: The tournament_id of this Game.
        :type tournament_id: int
        """

        self._tournament_id = tournament_id

    @property
    def under_payout(self):
        """Gets the under_payout of this Game.


        :return: The under_payout of this Game.
        :rtype: int
        """
        return self._under_payout

    @under_payout.setter
    def under_payout(self, under_payout):
        """Sets the under_payout of this Game.


        :param under_payout: The under_payout of this Game.
        :type under_payout: int
        """

        self._under_payout = under_payout

    @property
    def updated(self):
        """Gets the updated of this Game.


        :return: The updated of this Game.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Game.


        :param updated: The updated of this Game.
        :type updated: str
        """

        self._updated = updated
