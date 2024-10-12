# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Bye(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, season: int=None, team: str=None, week: int=None):
        """Bye - a model defined in OpenAPI

        :param season: The season of this Bye.
        :param team: The team of this Bye.
        :param week: The week of this Bye.
        """
        self.openapi_types = {
            'season': int,
            'team': str,
            'week': int
        }

        self.attribute_map = {
            'season': 'Season',
            'team': 'Team',
            'week': 'Week'
        }

        self._season = season
        self._team = team
        self._week = week

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Bye':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Bye of this Bye.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def season(self):
        """Gets the season of this Bye.


        :return: The season of this Bye.
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this Bye.


        :param season: The season of this Bye.
        :type season: int
        """

        self._season = season

    @property
    def team(self):
        """Gets the team of this Bye.


        :return: The team of this Bye.
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this Bye.


        :param team: The team of this Bye.
        :type team: str
        """

        self._team = team

    @property
    def week(self):
        """Gets the week of this Bye.


        :return: The week of this Bye.
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this Bye.


        :param week: The week of this Bye.
        :type week: int
        """

        self._week = week
