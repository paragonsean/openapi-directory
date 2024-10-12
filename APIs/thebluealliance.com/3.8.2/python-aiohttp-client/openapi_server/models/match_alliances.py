# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.match_alliance import MatchAlliance
from openapi_server import util


class MatchAlliances(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, blue: MatchAlliance=None, red: MatchAlliance=None):
        """MatchAlliances - a model defined in OpenAPI

        :param blue: The blue of this MatchAlliances.
        :param red: The red of this MatchAlliances.
        """
        self.openapi_types = {
            'blue': MatchAlliance,
            'red': MatchAlliance
        }

        self.attribute_map = {
            'blue': 'blue',
            'red': 'red'
        }

        self._blue = blue
        self._red = red

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MatchAlliances':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Match_alliances of this MatchAlliances.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def blue(self):
        """Gets the blue of this MatchAlliances.


        :return: The blue of this MatchAlliances.
        :rtype: MatchAlliance
        """
        return self._blue

    @blue.setter
    def blue(self, blue):
        """Sets the blue of this MatchAlliances.


        :param blue: The blue of this MatchAlliances.
        :type blue: MatchAlliance
        """

        self._blue = blue

    @property
    def red(self):
        """Gets the red of this MatchAlliances.


        :return: The red of this MatchAlliances.
        :rtype: MatchAlliance
        """
        return self._red

    @red.setter
    def red(self, red):
        """Sets the red of this MatchAlliances.


        :param red: The red of this MatchAlliances.
        :type red: MatchAlliance
        """

        self._red = red
