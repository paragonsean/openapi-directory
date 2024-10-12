# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RefreshAccessToken(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, grant_type: str=None, refresh_token: str=None):
        """RefreshAccessToken - a model defined in OpenAPI

        :param grant_type: The grant_type of this RefreshAccessToken.
        :param refresh_token: The refresh_token of this RefreshAccessToken.
        """
        self.openapi_types = {
            'grant_type': str,
            'refresh_token': str
        }

        self.attribute_map = {
            'grant_type': 'grant_type',
            'refresh_token': 'refresh_Token'
        }

        self._grant_type = grant_type
        self._refresh_token = refresh_token

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RefreshAccessToken':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RefreshAccessToken of this RefreshAccessToken.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def grant_type(self):
        """Gets the grant_type of this RefreshAccessToken.


        :return: The grant_type of this RefreshAccessToken.
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """Sets the grant_type of this RefreshAccessToken.


        :param grant_type: The grant_type of this RefreshAccessToken.
        :type grant_type: str
        """
        if grant_type is None:
            raise ValueError("Invalid value for `grant_type`, must not be `None`")

        self._grant_type = grant_type

    @property
    def refresh_token(self):
        """Gets the refresh_token of this RefreshAccessToken.


        :return: The refresh_token of this RefreshAccessToken.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this RefreshAccessToken.


        :param refresh_token: The refresh_token of this RefreshAccessToken.
        :type refresh_token: str
        """
        if refresh_token is None:
            raise ValueError("Invalid value for `refresh_token`, must not be `None`")

        self._refresh_token = refresh_token
