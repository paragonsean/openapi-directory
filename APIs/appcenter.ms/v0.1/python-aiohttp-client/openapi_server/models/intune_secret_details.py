# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class IntuneSecretDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id_token: str=None, refresh_token: str=None, refresh_token_expiry: str=None):
        """IntuneSecretDetails - a model defined in OpenAPI

        :param id_token: The id_token of this IntuneSecretDetails.
        :param refresh_token: The refresh_token of this IntuneSecretDetails.
        :param refresh_token_expiry: The refresh_token_expiry of this IntuneSecretDetails.
        """
        self.openapi_types = {
            'id_token': str,
            'refresh_token': str,
            'refresh_token_expiry': str
        }

        self.attribute_map = {
            'id_token': 'id_token',
            'refresh_token': 'refresh_token',
            'refresh_token_expiry': 'refresh_token_expiry'
        }

        self._id_token = id_token
        self._refresh_token = refresh_token
        self._refresh_token_expiry = refresh_token_expiry

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IntuneSecretDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IntuneSecretDetails of this IntuneSecretDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id_token(self):
        """Gets the id_token of this IntuneSecretDetails.

        the id token of user

        :return: The id_token of this IntuneSecretDetails.
        :rtype: str
        """
        return self._id_token

    @id_token.setter
    def id_token(self, id_token):
        """Sets the id_token of this IntuneSecretDetails.

        the id token of user

        :param id_token: The id_token of this IntuneSecretDetails.
        :type id_token: str
        """

        self._id_token = id_token

    @property
    def refresh_token(self):
        """Gets the refresh_token of this IntuneSecretDetails.

        the refresh token for user

        :return: The refresh_token of this IntuneSecretDetails.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this IntuneSecretDetails.

        the refresh token for user

        :param refresh_token: The refresh_token of this IntuneSecretDetails.
        :type refresh_token: str
        """

        self._refresh_token = refresh_token

    @property
    def refresh_token_expiry(self):
        """Gets the refresh_token_expiry of this IntuneSecretDetails.

        the expiry of refresh token

        :return: The refresh_token_expiry of this IntuneSecretDetails.
        :rtype: str
        """
        return self._refresh_token_expiry

    @refresh_token_expiry.setter
    def refresh_token_expiry(self, refresh_token_expiry):
        """Sets the refresh_token_expiry of this IntuneSecretDetails.

        the expiry of refresh token

        :param refresh_token_expiry: The refresh_token_expiry of this IntuneSecretDetails.
        :type refresh_token_expiry: str
        """

        self._refresh_token_expiry = refresh_token_expiry
