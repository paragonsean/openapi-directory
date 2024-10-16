# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.match_score_breakdown2017_alliance import MatchScoreBreakdown2017Alliance
from openapi_server import util


class MatchScoreBreakdown2017(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, blue: MatchScoreBreakdown2017Alliance=None, red: MatchScoreBreakdown2017Alliance=None):
        """MatchScoreBreakdown2017 - a model defined in OpenAPI

        :param blue: The blue of this MatchScoreBreakdown2017.
        :param red: The red of this MatchScoreBreakdown2017.
        """
        self.openapi_types = {
            'blue': MatchScoreBreakdown2017Alliance,
            'red': MatchScoreBreakdown2017Alliance
        }

        self.attribute_map = {
            'blue': 'blue',
            'red': 'red'
        }

        self._blue = blue
        self._red = red

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MatchScoreBreakdown2017':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Match_Score_Breakdown_2017 of this MatchScoreBreakdown2017.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def blue(self):
        """Gets the blue of this MatchScoreBreakdown2017.


        :return: The blue of this MatchScoreBreakdown2017.
        :rtype: MatchScoreBreakdown2017Alliance
        """
        return self._blue

    @blue.setter
    def blue(self, blue):
        """Sets the blue of this MatchScoreBreakdown2017.


        :param blue: The blue of this MatchScoreBreakdown2017.
        :type blue: MatchScoreBreakdown2017Alliance
        """

        self._blue = blue

    @property
    def red(self):
        """Gets the red of this MatchScoreBreakdown2017.


        :return: The red of this MatchScoreBreakdown2017.
        :rtype: MatchScoreBreakdown2017Alliance
        """
        return self._red

    @red.setter
    def red(self, red):
        """Sets the red of this MatchScoreBreakdown2017.


        :param red: The red of this MatchScoreBreakdown2017.
        :type red: MatchScoreBreakdown2017Alliance
        """

        self._red = red
