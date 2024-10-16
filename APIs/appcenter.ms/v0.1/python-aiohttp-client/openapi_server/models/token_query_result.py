# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TokenQueryResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, tokens: List[str]=None):
        """TokenQueryResult - a model defined in OpenAPI

        :param tokens: The tokens of this TokenQueryResult.
        """
        self.openapi_types = {
            'tokens': List[str]
        }

        self.attribute_map = {
            'tokens': 'tokens'
        }

        self._tokens = tokens

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TokenQueryResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TokenQueryResult of this TokenQueryResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tokens(self):
        """Gets the tokens of this TokenQueryResult.

        List of tokens.

        :return: The tokens of this TokenQueryResult.
        :rtype: List[str]
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """Sets the tokens of this TokenQueryResult.

        List of tokens.

        :param tokens: The tokens of this TokenQueryResult.
        :type tokens: List[str]
        """

        self._tokens = tokens
