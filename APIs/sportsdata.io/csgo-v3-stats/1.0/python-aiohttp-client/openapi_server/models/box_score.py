# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.game import Game
from openapi_server.models.map import Map
from openapi_server import util


class BoxScore(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, game: Game=None, maps: List[Map]=None):
        """BoxScore - a model defined in OpenAPI

        :param game: The game of this BoxScore.
        :param maps: The maps of this BoxScore.
        """
        self.openapi_types = {
            'game': Game,
            'maps': List[Map]
        }

        self.attribute_map = {
            'game': 'Game',
            'maps': 'Maps'
        }

        self._game = game
        self._maps = maps

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BoxScore':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BoxScore of this BoxScore.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def game(self):
        """Gets the game of this BoxScore.


        :return: The game of this BoxScore.
        :rtype: Game
        """
        return self._game

    @game.setter
    def game(self, game):
        """Sets the game of this BoxScore.


        :param game: The game of this BoxScore.
        :type game: Game
        """

        self._game = game

    @property
    def maps(self):
        """Gets the maps of this BoxScore.


        :return: The maps of this BoxScore.
        :rtype: List[Map]
        """
        return self._maps

    @maps.setter
    def maps(self, maps):
        """Sets the maps of this BoxScore.


        :param maps: The maps of this BoxScore.
        :type maps: List[Map]
        """

        self._maps = maps
