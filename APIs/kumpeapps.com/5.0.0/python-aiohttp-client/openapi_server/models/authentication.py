# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.user import User
from openapi_server import util


class Authentication(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, api_key: str=None, success: int=None, user: User=None):
        """Authentication - a model defined in OpenAPI

        :param api_key: The api_key of this Authentication.
        :param success: The success of this Authentication.
        :param user: The user of this Authentication.
        """
        self.openapi_types = {
            'api_key': str,
            'success': int,
            'user': User
        }

        self.attribute_map = {
            'api_key': 'apiKey',
            'success': 'success',
            'user': 'user'
        }

        self._api_key = api_key
        self._success = success
        self._user = user

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Authentication':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The authentication of this Authentication.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_key(self):
        """Gets the api_key of this Authentication.


        :return: The api_key of this Authentication.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this Authentication.


        :param api_key: The api_key of this Authentication.
        :type api_key: str
        """

        self._api_key = api_key

    @property
    def success(self):
        """Gets the success of this Authentication.


        :return: The success of this Authentication.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this Authentication.


        :param success: The success of this Authentication.
        :type success: int
        """

        self._success = success

    @property
    def user(self):
        """Gets the user of this Authentication.


        :return: The user of this Authentication.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Authentication.


        :param user: The user of this Authentication.
        :type user: User
        """

        self._user = user
