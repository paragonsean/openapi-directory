# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PhraseInsertVersion(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, weight: float=None):
        """PhraseInsertVersion - a model defined in OpenAPI

        :param name: The name of this PhraseInsertVersion.
        :param weight: The weight of this PhraseInsertVersion.
        """
        self.openapi_types = {
            'name': str,
            'weight': float
        }

        self.attribute_map = {
            'name': 'name',
            'weight': 'weight'
        }

        self._name = name
        self._weight = weight

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PhraseInsertVersion':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Phrase_InsertVersion of this PhraseInsertVersion.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this PhraseInsertVersion.

        Sentiment-bearing phrase name

        :return: The name of this PhraseInsertVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhraseInsertVersion.

        Sentiment-bearing phrase name

        :param name: The name of this PhraseInsertVersion.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def weight(self):
        """Gets the weight of this PhraseInsertVersion.

        Sentiment-bearing phrase weight

        :return: The weight of this PhraseInsertVersion.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this PhraseInsertVersion.

        Sentiment-bearing phrase weight

        :param weight: The weight of this PhraseInsertVersion.
        :type weight: float
        """
        if weight is None:
            raise ValueError("Invalid value for `weight`, must not be `None`")

        self._weight = weight
