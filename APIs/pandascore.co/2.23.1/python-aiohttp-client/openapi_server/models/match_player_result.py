# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class MatchPlayerResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, player_id: int=None, score: int=None):
        """MatchPlayerResult - a model defined in OpenAPI

        :param player_id: The player_id of this MatchPlayerResult.
        :param score: The score of this MatchPlayerResult.
        """
        self.openapi_types = {
            'player_id': int,
            'score': int
        }

        self.attribute_map = {
            'player_id': 'player_id',
            'score': 'score'
        }

        self._player_id = player_id
        self._score = score

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MatchPlayerResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MatchPlayerResult of this MatchPlayerResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def player_id(self):
        """Gets the player_id of this MatchPlayerResult.


        :return: The player_id of this MatchPlayerResult.
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this MatchPlayerResult.


        :param player_id: The player_id of this MatchPlayerResult.
        :type player_id: int
        """
        if player_id is None:
            raise ValueError("Invalid value for `player_id`, must not be `None`")
        if player_id is not None and player_id < 1:
            raise ValueError("Invalid value for `player_id`, must be a value greater than or equal to `1`")

        self._player_id = player_id

    @property
    def score(self):
        """Gets the score of this MatchPlayerResult.


        :return: The score of this MatchPlayerResult.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this MatchPlayerResult.


        :param score: The score of this MatchPlayerResult.
        :type score: int
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")
        if score is not None and score < 0:
            raise ValueError("Invalid value for `score`, must be a value greater than or equal to `0`")

        self._score = score
