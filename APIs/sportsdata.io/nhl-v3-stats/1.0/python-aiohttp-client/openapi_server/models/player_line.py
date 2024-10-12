# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PlayerLine(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, line_number: int=None, line_type: str=None, name: str=None, player_id: int=None, position: str=None, shoots: str=None):
        """PlayerLine - a model defined in OpenAPI

        :param line_number: The line_number of this PlayerLine.
        :param line_type: The line_type of this PlayerLine.
        :param name: The name of this PlayerLine.
        :param player_id: The player_id of this PlayerLine.
        :param position: The position of this PlayerLine.
        :param shoots: The shoots of this PlayerLine.
        """
        self.openapi_types = {
            'line_number': int,
            'line_type': str,
            'name': str,
            'player_id': int,
            'position': str,
            'shoots': str
        }

        self.attribute_map = {
            'line_number': 'LineNumber',
            'line_type': 'LineType',
            'name': 'Name',
            'player_id': 'PlayerID',
            'position': 'Position',
            'shoots': 'Shoots'
        }

        self._line_number = line_number
        self._line_type = line_type
        self._name = name
        self._player_id = player_id
        self._position = position
        self._shoots = shoots

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PlayerLine':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PlayerLine of this PlayerLine.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def line_number(self):
        """Gets the line_number of this PlayerLine.


        :return: The line_number of this PlayerLine.
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """Sets the line_number of this PlayerLine.


        :param line_number: The line_number of this PlayerLine.
        :type line_number: int
        """

        self._line_number = line_number

    @property
    def line_type(self):
        """Gets the line_type of this PlayerLine.


        :return: The line_type of this PlayerLine.
        :rtype: str
        """
        return self._line_type

    @line_type.setter
    def line_type(self, line_type):
        """Sets the line_type of this PlayerLine.


        :param line_type: The line_type of this PlayerLine.
        :type line_type: str
        """

        self._line_type = line_type

    @property
    def name(self):
        """Gets the name of this PlayerLine.


        :return: The name of this PlayerLine.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerLine.


        :param name: The name of this PlayerLine.
        :type name: str
        """

        self._name = name

    @property
    def player_id(self):
        """Gets the player_id of this PlayerLine.


        :return: The player_id of this PlayerLine.
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this PlayerLine.


        :param player_id: The player_id of this PlayerLine.
        :type player_id: int
        """

        self._player_id = player_id

    @property
    def position(self):
        """Gets the position of this PlayerLine.


        :return: The position of this PlayerLine.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PlayerLine.


        :param position: The position of this PlayerLine.
        :type position: str
        """

        self._position = position

    @property
    def shoots(self):
        """Gets the shoots of this PlayerLine.


        :return: The shoots of this PlayerLine.
        :rtype: str
        """
        return self._shoots

    @shoots.setter
    def shoots(self, shoots):
        """Sets the shoots of this PlayerLine.


        :param shoots: The shoots of this PlayerLine.
        :type shoots: str
        """

        self._shoots = shoots
