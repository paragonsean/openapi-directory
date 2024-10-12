# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Injury(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, body_part: str=None, declared_inactive: bool=None, injury_id: int=None, name: str=None, number: int=None, opponent: str=None, opponent_id: int=None, player_id: int=None, position: str=None, practice: str=None, practice_description: str=None, season: int=None, season_type: int=None, status: str=None, team: str=None, team_id: int=None, updated: str=None, week: int=None):
        """Injury - a model defined in OpenAPI

        :param body_part: The body_part of this Injury.
        :param declared_inactive: The declared_inactive of this Injury.
        :param injury_id: The injury_id of this Injury.
        :param name: The name of this Injury.
        :param number: The number of this Injury.
        :param opponent: The opponent of this Injury.
        :param opponent_id: The opponent_id of this Injury.
        :param player_id: The player_id of this Injury.
        :param position: The position of this Injury.
        :param practice: The practice of this Injury.
        :param practice_description: The practice_description of this Injury.
        :param season: The season of this Injury.
        :param season_type: The season_type of this Injury.
        :param status: The status of this Injury.
        :param team: The team of this Injury.
        :param team_id: The team_id of this Injury.
        :param updated: The updated of this Injury.
        :param week: The week of this Injury.
        """
        self.openapi_types = {
            'body_part': str,
            'declared_inactive': bool,
            'injury_id': int,
            'name': str,
            'number': int,
            'opponent': str,
            'opponent_id': int,
            'player_id': int,
            'position': str,
            'practice': str,
            'practice_description': str,
            'season': int,
            'season_type': int,
            'status': str,
            'team': str,
            'team_id': int,
            'updated': str,
            'week': int
        }

        self.attribute_map = {
            'body_part': 'BodyPart',
            'declared_inactive': 'DeclaredInactive',
            'injury_id': 'InjuryID',
            'name': 'Name',
            'number': 'Number',
            'opponent': 'Opponent',
            'opponent_id': 'OpponentID',
            'player_id': 'PlayerID',
            'position': 'Position',
            'practice': 'Practice',
            'practice_description': 'PracticeDescription',
            'season': 'Season',
            'season_type': 'SeasonType',
            'status': 'Status',
            'team': 'Team',
            'team_id': 'TeamID',
            'updated': 'Updated',
            'week': 'Week'
        }

        self._body_part = body_part
        self._declared_inactive = declared_inactive
        self._injury_id = injury_id
        self._name = name
        self._number = number
        self._opponent = opponent
        self._opponent_id = opponent_id
        self._player_id = player_id
        self._position = position
        self._practice = practice
        self._practice_description = practice_description
        self._season = season
        self._season_type = season_type
        self._status = status
        self._team = team
        self._team_id = team_id
        self._updated = updated
        self._week = week

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Injury':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Injury of this Injury.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def body_part(self):
        """Gets the body_part of this Injury.


        :return: The body_part of this Injury.
        :rtype: str
        """
        return self._body_part

    @body_part.setter
    def body_part(self, body_part):
        """Sets the body_part of this Injury.


        :param body_part: The body_part of this Injury.
        :type body_part: str
        """

        self._body_part = body_part

    @property
    def declared_inactive(self):
        """Gets the declared_inactive of this Injury.


        :return: The declared_inactive of this Injury.
        :rtype: bool
        """
        return self._declared_inactive

    @declared_inactive.setter
    def declared_inactive(self, declared_inactive):
        """Sets the declared_inactive of this Injury.


        :param declared_inactive: The declared_inactive of this Injury.
        :type declared_inactive: bool
        """

        self._declared_inactive = declared_inactive

    @property
    def injury_id(self):
        """Gets the injury_id of this Injury.


        :return: The injury_id of this Injury.
        :rtype: int
        """
        return self._injury_id

    @injury_id.setter
    def injury_id(self, injury_id):
        """Sets the injury_id of this Injury.


        :param injury_id: The injury_id of this Injury.
        :type injury_id: int
        """

        self._injury_id = injury_id

    @property
    def name(self):
        """Gets the name of this Injury.


        :return: The name of this Injury.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Injury.


        :param name: The name of this Injury.
        :type name: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this Injury.


        :return: The number of this Injury.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Injury.


        :param number: The number of this Injury.
        :type number: int
        """

        self._number = number

    @property
    def opponent(self):
        """Gets the opponent of this Injury.


        :return: The opponent of this Injury.
        :rtype: str
        """
        return self._opponent

    @opponent.setter
    def opponent(self, opponent):
        """Sets the opponent of this Injury.


        :param opponent: The opponent of this Injury.
        :type opponent: str
        """

        self._opponent = opponent

    @property
    def opponent_id(self):
        """Gets the opponent_id of this Injury.


        :return: The opponent_id of this Injury.
        :rtype: int
        """
        return self._opponent_id

    @opponent_id.setter
    def opponent_id(self, opponent_id):
        """Sets the opponent_id of this Injury.


        :param opponent_id: The opponent_id of this Injury.
        :type opponent_id: int
        """

        self._opponent_id = opponent_id

    @property
    def player_id(self):
        """Gets the player_id of this Injury.


        :return: The player_id of this Injury.
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this Injury.


        :param player_id: The player_id of this Injury.
        :type player_id: int
        """

        self._player_id = player_id

    @property
    def position(self):
        """Gets the position of this Injury.


        :return: The position of this Injury.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Injury.


        :param position: The position of this Injury.
        :type position: str
        """

        self._position = position

    @property
    def practice(self):
        """Gets the practice of this Injury.


        :return: The practice of this Injury.
        :rtype: str
        """
        return self._practice

    @practice.setter
    def practice(self, practice):
        """Sets the practice of this Injury.


        :param practice: The practice of this Injury.
        :type practice: str
        """

        self._practice = practice

    @property
    def practice_description(self):
        """Gets the practice_description of this Injury.


        :return: The practice_description of this Injury.
        :rtype: str
        """
        return self._practice_description

    @practice_description.setter
    def practice_description(self, practice_description):
        """Sets the practice_description of this Injury.


        :param practice_description: The practice_description of this Injury.
        :type practice_description: str
        """

        self._practice_description = practice_description

    @property
    def season(self):
        """Gets the season of this Injury.


        :return: The season of this Injury.
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this Injury.


        :param season: The season of this Injury.
        :type season: int
        """

        self._season = season

    @property
    def season_type(self):
        """Gets the season_type of this Injury.


        :return: The season_type of this Injury.
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this Injury.


        :param season_type: The season_type of this Injury.
        :type season_type: int
        """

        self._season_type = season_type

    @property
    def status(self):
        """Gets the status of this Injury.


        :return: The status of this Injury.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Injury.


        :param status: The status of this Injury.
        :type status: str
        """

        self._status = status

    @property
    def team(self):
        """Gets the team of this Injury.


        :return: The team of this Injury.
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this Injury.


        :param team: The team of this Injury.
        :type team: str
        """

        self._team = team

    @property
    def team_id(self):
        """Gets the team_id of this Injury.


        :return: The team_id of this Injury.
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this Injury.


        :param team_id: The team_id of this Injury.
        :type team_id: int
        """

        self._team_id = team_id

    @property
    def updated(self):
        """Gets the updated of this Injury.


        :return: The updated of this Injury.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Injury.


        :param updated: The updated of this Injury.
        :type updated: str
        """

        self._updated = updated

    @property
    def week(self):
        """Gets the week of this Injury.


        :return: The week of this Injury.
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this Injury.


        :param week: The week of this Injury.
        :type week: int
        """

        self._week = week
