# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class IdentityProviderUpdateRequestProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, client_id: str=None, client_secret: str=None):
        """IdentityProviderUpdateRequestProperties - a model defined in OpenAPI

        :param client_id: The client_id of this IdentityProviderUpdateRequestProperties.
        :param client_secret: The client_secret of this IdentityProviderUpdateRequestProperties.
        """
        self.openapi_types = {
            'client_id': str,
            'client_secret': str
        }

        self.attribute_map = {
            'client_id': 'clientId',
            'client_secret': 'clientSecret'
        }

        self._client_id = client_id
        self._client_secret = client_secret

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IdentityProviderUpdateRequestProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IdentityProvider_Update_request_properties of this IdentityProviderUpdateRequestProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client_id(self):
        """Gets the client_id of this IdentityProviderUpdateRequestProperties.

        Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.

        :return: The client_id of this IdentityProviderUpdateRequestProperties.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this IdentityProviderUpdateRequestProperties.

        Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.

        :param client_id: The client_id of this IdentityProviderUpdateRequestProperties.
        :type client_id: str
        """
        if client_id is not None and len(client_id) < 1:
            raise ValueError("Invalid value for `client_id`, length must be greater than or equal to `1`")

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this IdentityProviderUpdateRequestProperties.

        Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft.

        :return: The client_secret of this IdentityProviderUpdateRequestProperties.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this IdentityProviderUpdateRequestProperties.

        Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft.

        :param client_secret: The client_secret of this IdentityProviderUpdateRequestProperties.
        :type client_secret: str
        """
        if client_secret is not None and len(client_secret) < 1:
            raise ValueError("Invalid value for `client_secret`, length must be greater than or equal to `1`")

        self._client_secret = client_secret
