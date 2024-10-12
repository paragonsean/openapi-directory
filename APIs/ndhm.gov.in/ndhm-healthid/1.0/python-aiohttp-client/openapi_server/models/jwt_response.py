# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class JwtResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, token: str=None):
        """JwtResponse - a model defined in OpenAPI

        :param token: The token of this JwtResponse.
        """
        self.openapi_types = {
            'token': str
        }

        self.attribute_map = {
            'token': 'token'
        }

        self._token = token

    @classmethod
    def from_dict(cls, dikt: dict) -> 'JwtResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The JwtResponse of this JwtResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self):
        """Gets the token of this JwtResponse.


        :return: The token of this JwtResponse.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this JwtResponse.


        :param token: The token of this JwtResponse.
        :type token: str
        """

        self._token = token
