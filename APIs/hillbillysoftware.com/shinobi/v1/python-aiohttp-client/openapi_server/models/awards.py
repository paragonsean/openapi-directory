# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Awards(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, category: str=None, nominee: str=None, type: str=None, winner: str=None, year: str=None):
        """Awards - a model defined in OpenAPI

        :param category: The category of this Awards.
        :param nominee: The nominee of this Awards.
        :param type: The type of this Awards.
        :param winner: The winner of this Awards.
        :param year: The year of this Awards.
        """
        self.openapi_types = {
            'category': str,
            'nominee': str,
            'type': str,
            'winner': str,
            'year': str
        }

        self.attribute_map = {
            'category': 'Category',
            'nominee': 'Nominee',
            'type': 'Type',
            'winner': 'Winner',
            'year': 'Year'
        }

        self._category = category
        self._nominee = nominee
        self._type = type
        self._winner = winner
        self._year = year

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Awards':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _Awards of this Awards.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def category(self):
        """Gets the category of this Awards.


        :return: The category of this Awards.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Awards.


        :param category: The category of this Awards.
        :type category: str
        """

        self._category = category

    @property
    def nominee(self):
        """Gets the nominee of this Awards.


        :return: The nominee of this Awards.
        :rtype: str
        """
        return self._nominee

    @nominee.setter
    def nominee(self, nominee):
        """Sets the nominee of this Awards.


        :param nominee: The nominee of this Awards.
        :type nominee: str
        """

        self._nominee = nominee

    @property
    def type(self):
        """Gets the type of this Awards.


        :return: The type of this Awards.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Awards.


        :param type: The type of this Awards.
        :type type: str
        """

        self._type = type

    @property
    def winner(self):
        """Gets the winner of this Awards.


        :return: The winner of this Awards.
        :rtype: str
        """
        return self._winner

    @winner.setter
    def winner(self, winner):
        """Sets the winner of this Awards.


        :param winner: The winner of this Awards.
        :type winner: str
        """

        self._winner = winner

    @property
    def year(self):
        """Gets the year of this Awards.


        :return: The year of this Awards.
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Awards.


        :param year: The year of this Awards.
        :type year: str
        """

        self._year = year
