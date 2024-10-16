# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Goal(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assisted_by_player_id1: int=None, assisted_by_player_id2: int=None, assisted_by_player_name1: str=None, assisted_by_player_name2: str=None, game_id: int=None, game_minute: int=None, game_minute_extra: int=None, goal_id: int=None, name: str=None, player_id: int=None, team_id: int=None, type: str=None):
        """Goal - a model defined in OpenAPI

        :param assisted_by_player_id1: The assisted_by_player_id1 of this Goal.
        :param assisted_by_player_id2: The assisted_by_player_id2 of this Goal.
        :param assisted_by_player_name1: The assisted_by_player_name1 of this Goal.
        :param assisted_by_player_name2: The assisted_by_player_name2 of this Goal.
        :param game_id: The game_id of this Goal.
        :param game_minute: The game_minute of this Goal.
        :param game_minute_extra: The game_minute_extra of this Goal.
        :param goal_id: The goal_id of this Goal.
        :param name: The name of this Goal.
        :param player_id: The player_id of this Goal.
        :param team_id: The team_id of this Goal.
        :param type: The type of this Goal.
        """
        self.openapi_types = {
            'assisted_by_player_id1': int,
            'assisted_by_player_id2': int,
            'assisted_by_player_name1': str,
            'assisted_by_player_name2': str,
            'game_id': int,
            'game_minute': int,
            'game_minute_extra': int,
            'goal_id': int,
            'name': str,
            'player_id': int,
            'team_id': int,
            'type': str
        }

        self.attribute_map = {
            'assisted_by_player_id1': 'AssistedByPlayerId1',
            'assisted_by_player_id2': 'AssistedByPlayerId2',
            'assisted_by_player_name1': 'AssistedByPlayerName1',
            'assisted_by_player_name2': 'AssistedByPlayerName2',
            'game_id': 'GameId',
            'game_minute': 'GameMinute',
            'game_minute_extra': 'GameMinuteExtra',
            'goal_id': 'GoalId',
            'name': 'Name',
            'player_id': 'PlayerId',
            'team_id': 'TeamId',
            'type': 'Type'
        }

        self._assisted_by_player_id1 = assisted_by_player_id1
        self._assisted_by_player_id2 = assisted_by_player_id2
        self._assisted_by_player_name1 = assisted_by_player_name1
        self._assisted_by_player_name2 = assisted_by_player_name2
        self._game_id = game_id
        self._game_minute = game_minute
        self._game_minute_extra = game_minute_extra
        self._goal_id = goal_id
        self._name = name
        self._player_id = player_id
        self._team_id = team_id
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Goal':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Goal of this Goal.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assisted_by_player_id1(self):
        """Gets the assisted_by_player_id1 of this Goal.


        :return: The assisted_by_player_id1 of this Goal.
        :rtype: int
        """
        return self._assisted_by_player_id1

    @assisted_by_player_id1.setter
    def assisted_by_player_id1(self, assisted_by_player_id1):
        """Sets the assisted_by_player_id1 of this Goal.


        :param assisted_by_player_id1: The assisted_by_player_id1 of this Goal.
        :type assisted_by_player_id1: int
        """

        self._assisted_by_player_id1 = assisted_by_player_id1

    @property
    def assisted_by_player_id2(self):
        """Gets the assisted_by_player_id2 of this Goal.


        :return: The assisted_by_player_id2 of this Goal.
        :rtype: int
        """
        return self._assisted_by_player_id2

    @assisted_by_player_id2.setter
    def assisted_by_player_id2(self, assisted_by_player_id2):
        """Sets the assisted_by_player_id2 of this Goal.


        :param assisted_by_player_id2: The assisted_by_player_id2 of this Goal.
        :type assisted_by_player_id2: int
        """

        self._assisted_by_player_id2 = assisted_by_player_id2

    @property
    def assisted_by_player_name1(self):
        """Gets the assisted_by_player_name1 of this Goal.


        :return: The assisted_by_player_name1 of this Goal.
        :rtype: str
        """
        return self._assisted_by_player_name1

    @assisted_by_player_name1.setter
    def assisted_by_player_name1(self, assisted_by_player_name1):
        """Sets the assisted_by_player_name1 of this Goal.


        :param assisted_by_player_name1: The assisted_by_player_name1 of this Goal.
        :type assisted_by_player_name1: str
        """

        self._assisted_by_player_name1 = assisted_by_player_name1

    @property
    def assisted_by_player_name2(self):
        """Gets the assisted_by_player_name2 of this Goal.


        :return: The assisted_by_player_name2 of this Goal.
        :rtype: str
        """
        return self._assisted_by_player_name2

    @assisted_by_player_name2.setter
    def assisted_by_player_name2(self, assisted_by_player_name2):
        """Sets the assisted_by_player_name2 of this Goal.


        :param assisted_by_player_name2: The assisted_by_player_name2 of this Goal.
        :type assisted_by_player_name2: str
        """

        self._assisted_by_player_name2 = assisted_by_player_name2

    @property
    def game_id(self):
        """Gets the game_id of this Goal.


        :return: The game_id of this Goal.
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this Goal.


        :param game_id: The game_id of this Goal.
        :type game_id: int
        """

        self._game_id = game_id

    @property
    def game_minute(self):
        """Gets the game_minute of this Goal.


        :return: The game_minute of this Goal.
        :rtype: int
        """
        return self._game_minute

    @game_minute.setter
    def game_minute(self, game_minute):
        """Sets the game_minute of this Goal.


        :param game_minute: The game_minute of this Goal.
        :type game_minute: int
        """

        self._game_minute = game_minute

    @property
    def game_minute_extra(self):
        """Gets the game_minute_extra of this Goal.


        :return: The game_minute_extra of this Goal.
        :rtype: int
        """
        return self._game_minute_extra

    @game_minute_extra.setter
    def game_minute_extra(self, game_minute_extra):
        """Sets the game_minute_extra of this Goal.


        :param game_minute_extra: The game_minute_extra of this Goal.
        :type game_minute_extra: int
        """

        self._game_minute_extra = game_minute_extra

    @property
    def goal_id(self):
        """Gets the goal_id of this Goal.


        :return: The goal_id of this Goal.
        :rtype: int
        """
        return self._goal_id

    @goal_id.setter
    def goal_id(self, goal_id):
        """Sets the goal_id of this Goal.


        :param goal_id: The goal_id of this Goal.
        :type goal_id: int
        """

        self._goal_id = goal_id

    @property
    def name(self):
        """Gets the name of this Goal.


        :return: The name of this Goal.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Goal.


        :param name: The name of this Goal.
        :type name: str
        """

        self._name = name

    @property
    def player_id(self):
        """Gets the player_id of this Goal.


        :return: The player_id of this Goal.
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this Goal.


        :param player_id: The player_id of this Goal.
        :type player_id: int
        """

        self._player_id = player_id

    @property
    def team_id(self):
        """Gets the team_id of this Goal.


        :return: The team_id of this Goal.
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this Goal.


        :param team_id: The team_id of this Goal.
        :type team_id: int
        """

        self._team_id = team_id

    @property
    def type(self):
        """Gets the type of this Goal.


        :return: The type of this Goal.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Goal.


        :param type: The type of this Goal.
        :type type: str
        """

        self._type = type
