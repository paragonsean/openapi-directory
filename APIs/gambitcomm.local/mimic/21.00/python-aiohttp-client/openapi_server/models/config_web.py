# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ConfigWEB(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, is_persistent_connections: int=None, password: str=None, port: int=None, rule: str=None, username: str=None, wsdl: str=None):
        """ConfigWEB - a model defined in OpenAPI

        :param is_persistent_connections: The is_persistent_connections of this ConfigWEB.
        :param password: The password of this ConfigWEB.
        :param port: The port of this ConfigWEB.
        :param rule: The rule of this ConfigWEB.
        :param username: The username of this ConfigWEB.
        :param wsdl: The wsdl of this ConfigWEB.
        """
        self.openapi_types = {
            'is_persistent_connections': int,
            'password': str,
            'port': int,
            'rule': str,
            'username': str,
            'wsdl': str
        }

        self.attribute_map = {
            'is_persistent_connections': 'is_persistent_connections',
            'password': 'password',
            'port': 'port',
            'rule': 'rule',
            'username': 'username',
            'wsdl': 'wsdl'
        }

        self._is_persistent_connections = is_persistent_connections
        self._password = password
        self._port = port
        self._rule = rule
        self._username = username
        self._wsdl = wsdl

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ConfigWEB':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ConfigWEB of this ConfigWEB.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def is_persistent_connections(self):
        """Gets the is_persistent_connections of this ConfigWEB.


        :return: The is_persistent_connections of this ConfigWEB.
        :rtype: int
        """
        return self._is_persistent_connections

    @is_persistent_connections.setter
    def is_persistent_connections(self, is_persistent_connections):
        """Sets the is_persistent_connections of this ConfigWEB.


        :param is_persistent_connections: The is_persistent_connections of this ConfigWEB.
        :type is_persistent_connections: int
        """

        self._is_persistent_connections = is_persistent_connections

    @property
    def password(self):
        """Gets the password of this ConfigWEB.


        :return: The password of this ConfigWEB.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ConfigWEB.


        :param password: The password of this ConfigWEB.
        :type password: str
        """

        self._password = password

    @property
    def port(self):
        """Gets the port of this ConfigWEB.


        :return: The port of this ConfigWEB.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ConfigWEB.


        :param port: The port of this ConfigWEB.
        :type port: int
        """

        self._port = port

    @property
    def rule(self):
        """Gets the rule of this ConfigWEB.


        :return: The rule of this ConfigWEB.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this ConfigWEB.


        :param rule: The rule of this ConfigWEB.
        :type rule: str
        """

        self._rule = rule

    @property
    def username(self):
        """Gets the username of this ConfigWEB.


        :return: The username of this ConfigWEB.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ConfigWEB.


        :param username: The username of this ConfigWEB.
        :type username: str
        """

        self._username = username

    @property
    def wsdl(self):
        """Gets the wsdl of this ConfigWEB.


        :return: The wsdl of this ConfigWEB.
        :rtype: str
        """
        return self._wsdl

    @wsdl.setter
    def wsdl(self, wsdl):
        """Sets the wsdl of this ConfigWEB.


        :param wsdl: The wsdl of this ConfigWEB.
        :type wsdl: str
        """

        self._wsdl = wsdl
