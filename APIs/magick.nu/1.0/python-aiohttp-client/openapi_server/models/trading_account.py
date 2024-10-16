# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TradingAccount(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, broker_server: str=None, magick_username: str=None, password: str=None, username: str=None):
        """TradingAccount - a model defined in OpenAPI

        :param broker_server: The broker_server of this TradingAccount.
        :param magick_username: The magick_username of this TradingAccount.
        :param password: The password of this TradingAccount.
        :param username: The username of this TradingAccount.
        """
        self.openapi_types = {
            'broker_server': str,
            'magick_username': str,
            'password': str,
            'username': str
        }

        self.attribute_map = {
            'broker_server': 'brokerServer',
            'magick_username': 'magickUsername',
            'password': 'password',
            'username': 'username'
        }

        self._broker_server = broker_server
        self._magick_username = magick_username
        self._password = password
        self._username = username

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TradingAccount':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TradingAccount of this TradingAccount.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def broker_server(self):
        """Gets the broker_server of this TradingAccount.


        :return: The broker_server of this TradingAccount.
        :rtype: str
        """
        return self._broker_server

    @broker_server.setter
    def broker_server(self, broker_server):
        """Sets the broker_server of this TradingAccount.


        :param broker_server: The broker_server of this TradingAccount.
        :type broker_server: str
        """

        self._broker_server = broker_server

    @property
    def magick_username(self):
        """Gets the magick_username of this TradingAccount.


        :return: The magick_username of this TradingAccount.
        :rtype: str
        """
        return self._magick_username

    @magick_username.setter
    def magick_username(self, magick_username):
        """Sets the magick_username of this TradingAccount.


        :param magick_username: The magick_username of this TradingAccount.
        :type magick_username: str
        """

        self._magick_username = magick_username

    @property
    def password(self):
        """Gets the password of this TradingAccount.


        :return: The password of this TradingAccount.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TradingAccount.


        :param password: The password of this TradingAccount.
        :type password: str
        """

        self._password = password

    @property
    def username(self):
        """Gets the username of this TradingAccount.


        :return: The username of this TradingAccount.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this TradingAccount.


        :param username: The username of this TradingAccount.
        :type username: str
        """

        self._username = username
