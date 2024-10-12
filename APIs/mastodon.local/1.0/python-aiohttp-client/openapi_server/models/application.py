# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Application(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, client_id: str=None, client_secret: str=None, name: str=None, vapid_key: str=None, website: str=None):
        """Application - a model defined in OpenAPI

        :param client_id: The client_id of this Application.
        :param client_secret: The client_secret of this Application.
        :param name: The name of this Application.
        :param vapid_key: The vapid_key of this Application.
        :param website: The website of this Application.
        """
        self.openapi_types = {
            'client_id': str,
            'client_secret': str,
            'name': str,
            'vapid_key': str,
            'website': str
        }

        self.attribute_map = {
            'client_id': 'client_id',
            'client_secret': 'client_secret',
            'name': 'name',
            'vapid_key': 'vapid_key',
            'website': 'website'
        }

        self._client_id = client_id
        self._client_secret = client_secret
        self._name = name
        self._vapid_key = vapid_key
        self._website = website

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Application':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Application of this Application.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client_id(self):
        """Gets the client_id of this Application.

        Client ID key, to be used for obtaining OAuth tokens

        :return: The client_id of this Application.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Application.

        Client ID key, to be used for obtaining OAuth tokens

        :param client_id: The client_id of this Application.
        :type client_id: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this Application.

        Client secret key, to be used for obtaining OAuth tokens

        :return: The client_secret of this Application.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this Application.

        Client secret key, to be used for obtaining OAuth tokens

        :param client_secret: The client_secret of this Application.
        :type client_secret: str
        """

        self._client_secret = client_secret

    @property
    def name(self):
        """Gets the name of this Application.

        The name of your application.

        :return: The name of this Application.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Application.

        The name of your application.

        :param name: The name of this Application.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def vapid_key(self):
        """Gets the vapid_key of this Application.

        Used for Push Streaming API. Returned with [POST /api/v1/apps](https://docs.joinmastodon.org/methods/apps/#create-an-application). Equivalent to [PushSubscription#server_key](https://docs.joinmastodon.org/entities/pushsubscription/#server_key)

        :return: The vapid_key of this Application.
        :rtype: str
        """
        return self._vapid_key

    @vapid_key.setter
    def vapid_key(self, vapid_key):
        """Sets the vapid_key of this Application.

        Used for Push Streaming API. Returned with [POST /api/v1/apps](https://docs.joinmastodon.org/methods/apps/#create-an-application). Equivalent to [PushSubscription#server_key](https://docs.joinmastodon.org/entities/pushsubscription/#server_key)

        :param vapid_key: The vapid_key of this Application.
        :type vapid_key: str
        """

        self._vapid_key = vapid_key

    @property
    def website(self):
        """Gets the website of this Application.

        The website associated with your application. Must be URL.

        :return: The website of this Application.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Application.

        The website associated with your application. Must be URL.

        :param website: The website of this Application.
        :type website: str
        """

        self._website = website
