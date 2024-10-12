# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Auth0Config(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, callback_url: str=None, client_id: str=None, client_secret: str=None, domain: str=None):
        """Auth0Config - a model defined in OpenAPI

        :param callback_url: The callback_url of this Auth0Config.
        :param client_id: The client_id of this Auth0Config.
        :param client_secret: The client_secret of this Auth0Config.
        :param domain: The domain of this Auth0Config.
        """
        self.openapi_types = {
            'callback_url': str,
            'client_id': str,
            'client_secret': str,
            'domain': str
        }

        self.attribute_map = {
            'callback_url': 'callbackUrl',
            'client_id': 'clientId',
            'client_secret': 'clientSecret',
            'domain': 'domain'
        }

        self._callback_url = callback_url
        self._client_id = client_id
        self._client_secret = client_secret
        self._domain = domain

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Auth0Config':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Auth0Config of this Auth0Config.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def callback_url(self):
        """Gets the callback_url of this Auth0Config.

        Auth0 callback URL

        :return: The callback_url of this Auth0Config.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this Auth0Config.

        Auth0 callback URL

        :param callback_url: The callback_url of this Auth0Config.
        :type callback_url: str
        """
        if callback_url is None:
            raise ValueError("Invalid value for `callback_url`, must not be `None`")

        self._callback_url = callback_url

    @property
    def client_id(self):
        """Gets the client_id of this Auth0Config.

        Auth0 client id

        :return: The client_id of this Auth0Config.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Auth0Config.

        Auth0 client id

        :param client_id: The client_id of this Auth0Config.
        :type client_id: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this Auth0Config.

        Auth0 client secret

        :return: The client_secret of this Auth0Config.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this Auth0Config.

        Auth0 client secret

        :param client_secret: The client_secret of this Auth0Config.
        :type client_secret: str
        """
        if client_secret is None:
            raise ValueError("Invalid value for `client_secret`, must not be `None`")

        self._client_secret = client_secret

    @property
    def domain(self):
        """Gets the domain of this Auth0Config.

        Auth0 domain

        :return: The domain of this Auth0Config.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Auth0Config.

        Auth0 domain

        :param domain: The domain of this Auth0Config.
        :type domain: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")

        self._domain = domain
