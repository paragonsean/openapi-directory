# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PlayerBasic(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, birth_city: str=None, birth_date: str=None, birth_state: str=None, first_name: str=None, global_team_id: int=None, height: int=None, jersey: int=None, last_name: str=None, player_id: int=None, position: str=None, status: str=None, team: str=None, team_id: int=None, weight: int=None):
        """PlayerBasic - a model defined in OpenAPI

        :param birth_city: The birth_city of this PlayerBasic.
        :param birth_date: The birth_date of this PlayerBasic.
        :param birth_state: The birth_state of this PlayerBasic.
        :param first_name: The first_name of this PlayerBasic.
        :param global_team_id: The global_team_id of this PlayerBasic.
        :param height: The height of this PlayerBasic.
        :param jersey: The jersey of this PlayerBasic.
        :param last_name: The last_name of this PlayerBasic.
        :param player_id: The player_id of this PlayerBasic.
        :param position: The position of this PlayerBasic.
        :param status: The status of this PlayerBasic.
        :param team: The team of this PlayerBasic.
        :param team_id: The team_id of this PlayerBasic.
        :param weight: The weight of this PlayerBasic.
        """
        self.openapi_types = {
            'birth_city': str,
            'birth_date': str,
            'birth_state': str,
            'first_name': str,
            'global_team_id': int,
            'height': int,
            'jersey': int,
            'last_name': str,
            'player_id': int,
            'position': str,
            'status': str,
            'team': str,
            'team_id': int,
            'weight': int
        }

        self.attribute_map = {
            'birth_city': 'BirthCity',
            'birth_date': 'BirthDate',
            'birth_state': 'BirthState',
            'first_name': 'FirstName',
            'global_team_id': 'GlobalTeamID',
            'height': 'Height',
            'jersey': 'Jersey',
            'last_name': 'LastName',
            'player_id': 'PlayerID',
            'position': 'Position',
            'status': 'Status',
            'team': 'Team',
            'team_id': 'TeamID',
            'weight': 'Weight'
        }

        self._birth_city = birth_city
        self._birth_date = birth_date
        self._birth_state = birth_state
        self._first_name = first_name
        self._global_team_id = global_team_id
        self._height = height
        self._jersey = jersey
        self._last_name = last_name
        self._player_id = player_id
        self._position = position
        self._status = status
        self._team = team
        self._team_id = team_id
        self._weight = weight

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PlayerBasic':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PlayerBasic of this PlayerBasic.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def birth_city(self):
        """Gets the birth_city of this PlayerBasic.


        :return: The birth_city of this PlayerBasic.
        :rtype: str
        """
        return self._birth_city

    @birth_city.setter
    def birth_city(self, birth_city):
        """Sets the birth_city of this PlayerBasic.


        :param birth_city: The birth_city of this PlayerBasic.
        :type birth_city: str
        """

        self._birth_city = birth_city

    @property
    def birth_date(self):
        """Gets the birth_date of this PlayerBasic.


        :return: The birth_date of this PlayerBasic.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this PlayerBasic.


        :param birth_date: The birth_date of this PlayerBasic.
        :type birth_date: str
        """

        self._birth_date = birth_date

    @property
    def birth_state(self):
        """Gets the birth_state of this PlayerBasic.


        :return: The birth_state of this PlayerBasic.
        :rtype: str
        """
        return self._birth_state

    @birth_state.setter
    def birth_state(self, birth_state):
        """Sets the birth_state of this PlayerBasic.


        :param birth_state: The birth_state of this PlayerBasic.
        :type birth_state: str
        """

        self._birth_state = birth_state

    @property
    def first_name(self):
        """Gets the first_name of this PlayerBasic.


        :return: The first_name of this PlayerBasic.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this PlayerBasic.


        :param first_name: The first_name of this PlayerBasic.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def global_team_id(self):
        """Gets the global_team_id of this PlayerBasic.


        :return: The global_team_id of this PlayerBasic.
        :rtype: int
        """
        return self._global_team_id

    @global_team_id.setter
    def global_team_id(self, global_team_id):
        """Sets the global_team_id of this PlayerBasic.


        :param global_team_id: The global_team_id of this PlayerBasic.
        :type global_team_id: int
        """

        self._global_team_id = global_team_id

    @property
    def height(self):
        """Gets the height of this PlayerBasic.


        :return: The height of this PlayerBasic.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this PlayerBasic.


        :param height: The height of this PlayerBasic.
        :type height: int
        """

        self._height = height

    @property
    def jersey(self):
        """Gets the jersey of this PlayerBasic.


        :return: The jersey of this PlayerBasic.
        :rtype: int
        """
        return self._jersey

    @jersey.setter
    def jersey(self, jersey):
        """Sets the jersey of this PlayerBasic.


        :param jersey: The jersey of this PlayerBasic.
        :type jersey: int
        """

        self._jersey = jersey

    @property
    def last_name(self):
        """Gets the last_name of this PlayerBasic.


        :return: The last_name of this PlayerBasic.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this PlayerBasic.


        :param last_name: The last_name of this PlayerBasic.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def player_id(self):
        """Gets the player_id of this PlayerBasic.


        :return: The player_id of this PlayerBasic.
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this PlayerBasic.


        :param player_id: The player_id of this PlayerBasic.
        :type player_id: int
        """

        self._player_id = player_id

    @property
    def position(self):
        """Gets the position of this PlayerBasic.


        :return: The position of this PlayerBasic.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PlayerBasic.


        :param position: The position of this PlayerBasic.
        :type position: str
        """

        self._position = position

    @property
    def status(self):
        """Gets the status of this PlayerBasic.


        :return: The status of this PlayerBasic.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PlayerBasic.


        :param status: The status of this PlayerBasic.
        :type status: str
        """

        self._status = status

    @property
    def team(self):
        """Gets the team of this PlayerBasic.


        :return: The team of this PlayerBasic.
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this PlayerBasic.


        :param team: The team of this PlayerBasic.
        :type team: str
        """

        self._team = team

    @property
    def team_id(self):
        """Gets the team_id of this PlayerBasic.


        :return: The team_id of this PlayerBasic.
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this PlayerBasic.


        :param team_id: The team_id of this PlayerBasic.
        :type team_id: int
        """

        self._team_id = team_id

    @property
    def weight(self):
        """Gets the weight of this PlayerBasic.


        :return: The weight of this PlayerBasic.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this PlayerBasic.


        :param weight: The weight of this PlayerBasic.
        :type weight: int
        """

        self._weight = weight
