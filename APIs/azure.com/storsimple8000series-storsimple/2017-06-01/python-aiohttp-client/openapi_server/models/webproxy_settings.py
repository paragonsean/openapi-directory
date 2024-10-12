# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class WebproxySettings(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, authentication: str=None, connection_uri: str=None, username: str=None):
        """WebproxySettings - a model defined in OpenAPI

        :param authentication: The authentication of this WebproxySettings.
        :param connection_uri: The connection_uri of this WebproxySettings.
        :param username: The username of this WebproxySettings.
        """
        self.openapi_types = {
            'authentication': str,
            'connection_uri': str,
            'username': str
        }

        self.attribute_map = {
            'authentication': 'authentication',
            'connection_uri': 'connectionUri',
            'username': 'username'
        }

        self._authentication = authentication
        self._connection_uri = connection_uri
        self._username = username

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WebproxySettings':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The WebproxySettings of this WebproxySettings.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def authentication(self):
        """Gets the authentication of this WebproxySettings.

        The authentication type.

        :return: The authentication of this WebproxySettings.
        :rtype: str
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this WebproxySettings.

        The authentication type.

        :param authentication: The authentication of this WebproxySettings.
        :type authentication: str
        """
        allowed_values = ["Invalid", "None", "Basic", "NTLM"]  # noqa: E501
        if authentication not in allowed_values:
            raise ValueError(
                "Invalid value for `authentication` ({0}), must be one of {1}"
                .format(authentication, allowed_values)
            )

        self._authentication = authentication

    @property
    def connection_uri(self):
        """Gets the connection_uri of this WebproxySettings.

        The connection URI.

        :return: The connection_uri of this WebproxySettings.
        :rtype: str
        """
        return self._connection_uri

    @connection_uri.setter
    def connection_uri(self, connection_uri):
        """Sets the connection_uri of this WebproxySettings.

        The connection URI.

        :param connection_uri: The connection_uri of this WebproxySettings.
        :type connection_uri: str
        """

        self._connection_uri = connection_uri

    @property
    def username(self):
        """Gets the username of this WebproxySettings.

        The webproxy username.

        :return: The username of this WebproxySettings.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this WebproxySettings.

        The webproxy username.

        :param username: The username of this WebproxySettings.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username
