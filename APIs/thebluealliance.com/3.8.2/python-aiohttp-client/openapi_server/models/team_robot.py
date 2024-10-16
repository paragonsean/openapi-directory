# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TeamRobot(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key: str=None, robot_name: str=None, team_key: str=None, year: int=None):
        """TeamRobot - a model defined in OpenAPI

        :param key: The key of this TeamRobot.
        :param robot_name: The robot_name of this TeamRobot.
        :param team_key: The team_key of this TeamRobot.
        :param year: The year of this TeamRobot.
        """
        self.openapi_types = {
            'key': str,
            'robot_name': str,
            'team_key': str,
            'year': int
        }

        self.attribute_map = {
            'key': 'key',
            'robot_name': 'robot_name',
            'team_key': 'team_key',
            'year': 'year'
        }

        self._key = key
        self._robot_name = robot_name
        self._team_key = team_key
        self._year = year

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TeamRobot':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Team_Robot of this TeamRobot.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self):
        """Gets the key of this TeamRobot.

        Internal TBA identifier for this robot.

        :return: The key of this TeamRobot.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TeamRobot.

        Internal TBA identifier for this robot.

        :param key: The key of this TeamRobot.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def robot_name(self):
        """Gets the robot_name of this TeamRobot.

        Name of the robot as provided by the team.

        :return: The robot_name of this TeamRobot.
        :rtype: str
        """
        return self._robot_name

    @robot_name.setter
    def robot_name(self, robot_name):
        """Sets the robot_name of this TeamRobot.

        Name of the robot as provided by the team.

        :param robot_name: The robot_name of this TeamRobot.
        :type robot_name: str
        """
        if robot_name is None:
            raise ValueError("Invalid value for `robot_name`, must not be `None`")

        self._robot_name = robot_name

    @property
    def team_key(self):
        """Gets the team_key of this TeamRobot.

        TBA team key for this robot.

        :return: The team_key of this TeamRobot.
        :rtype: str
        """
        return self._team_key

    @team_key.setter
    def team_key(self, team_key):
        """Sets the team_key of this TeamRobot.

        TBA team key for this robot.

        :param team_key: The team_key of this TeamRobot.
        :type team_key: str
        """
        if team_key is None:
            raise ValueError("Invalid value for `team_key`, must not be `None`")

        self._team_key = team_key

    @property
    def year(self):
        """Gets the year of this TeamRobot.

        Year this robot competed in.

        :return: The year of this TeamRobot.
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this TeamRobot.

        Year this robot competed in.

        :param year: The year of this TeamRobot.
        :type year: int
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")

        self._year = year
