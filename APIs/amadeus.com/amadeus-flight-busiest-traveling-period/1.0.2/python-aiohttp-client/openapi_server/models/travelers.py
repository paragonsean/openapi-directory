# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Travelers(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, score: float=None):
        """Travelers - a model defined in OpenAPI

        :param score: The score of this Travelers.
        """
        self.openapi_types = {
            'score': float
        }

        self.attribute_map = {
            'score': 'score'
        }

        self._score = score

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Travelers':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Travelers of this Travelers.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def score(self):
        """Gets the score of this Travelers.

        Approximate score for ranking purposes calculated based on number of travelers in the location.

        :return: The score of this Travelers.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Travelers.

        Approximate score for ranking purposes calculated based on number of travelers in the location.

        :param score: The score of this Travelers.
        :type score: float
        """

        self._score = score
