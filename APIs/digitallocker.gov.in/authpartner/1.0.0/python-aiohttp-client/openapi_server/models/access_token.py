# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AccessToken(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, client_id: str=None, client_secret: str=None, code: str=None, code_verifier: str=None, grant_type: str=None, redirect_uri: str=None):
        """AccessToken - a model defined in OpenAPI

        :param client_id: The client_id of this AccessToken.
        :param client_secret: The client_secret of this AccessToken.
        :param code: The code of this AccessToken.
        :param code_verifier: The code_verifier of this AccessToken.
        :param grant_type: The grant_type of this AccessToken.
        :param redirect_uri: The redirect_uri of this AccessToken.
        """
        self.openapi_types = {
            'client_id': str,
            'client_secret': str,
            'code': str,
            'code_verifier': str,
            'grant_type': str,
            'redirect_uri': str
        }

        self.attribute_map = {
            'client_id': 'client_id',
            'client_secret': 'client_secret',
            'code': 'code',
            'code_verifier': 'code_verifier',
            'grant_type': 'grant_type',
            'redirect_uri': 'redirect_uri'
        }

        self._client_id = client_id
        self._client_secret = client_secret
        self._code = code
        self._code_verifier = code_verifier
        self._grant_type = grant_type
        self._redirect_uri = redirect_uri

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AccessToken':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AccessToken of this AccessToken.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client_id(self):
        """Gets the client_id of this AccessToken.


        :return: The client_id of this AccessToken.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AccessToken.


        :param client_id: The client_id of this AccessToken.
        :type client_id: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this AccessToken.


        :return: The client_secret of this AccessToken.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this AccessToken.


        :param client_secret: The client_secret of this AccessToken.
        :type client_secret: str
        """
        if client_secret is None:
            raise ValueError("Invalid value for `client_secret`, must not be `None`")

        self._client_secret = client_secret

    @property
    def code(self):
        """Gets the code of this AccessToken.


        :return: The code of this AccessToken.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AccessToken.


        :param code: The code of this AccessToken.
        :type code: str
        """

        self._code = code

    @property
    def code_verifier(self):
        """Gets the code_verifier of this AccessToken.


        :return: The code_verifier of this AccessToken.
        :rtype: str
        """
        return self._code_verifier

    @code_verifier.setter
    def code_verifier(self, code_verifier):
        """Sets the code_verifier of this AccessToken.


        :param code_verifier: The code_verifier of this AccessToken.
        :type code_verifier: str
        """

        self._code_verifier = code_verifier

    @property
    def grant_type(self):
        """Gets the grant_type of this AccessToken.


        :return: The grant_type of this AccessToken.
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """Sets the grant_type of this AccessToken.


        :param grant_type: The grant_type of this AccessToken.
        :type grant_type: str
        """
        allowed_values = ["authorization_code"]  # noqa: E501
        if grant_type not in allowed_values:
            raise ValueError(
                "Invalid value for `grant_type` ({0}), must be one of {1}"
                .format(grant_type, allowed_values)
            )

        self._grant_type = grant_type

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this AccessToken.


        :return: The redirect_uri of this AccessToken.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this AccessToken.


        :param redirect_uri: The redirect_uri of this AccessToken.
        :type redirect_uri: str
        """

        self._redirect_uri = redirect_uri
