# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateAliasRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, destinations: List[str]=None, email_address: str=None):
        """CreateAliasRequest - a model defined in OpenAPI

        :param destinations: The destinations of this CreateAliasRequest.
        :param email_address: The email_address of this CreateAliasRequest.
        """
        self.openapi_types = {
            'destinations': List[str],
            'email_address': str
        }

        self.attribute_map = {
            'destinations': 'destinations',
            'email_address': 'email_address'
        }

        self._destinations = destinations
        self._email_address = email_address

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateAliasRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CreateAliasRequest of this CreateAliasRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def destinations(self):
        """Gets the destinations of this CreateAliasRequest.

        The alias destination e-mail addresses

        :return: The destinations of this CreateAliasRequest.
        :rtype: List[str]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this CreateAliasRequest.

        The alias destination e-mail addresses

        :param destinations: The destinations of this CreateAliasRequest.
        :type destinations: List[str]
        """

        self._destinations = destinations

    @property
    def email_address(self):
        """Gets the email_address of this CreateAliasRequest.

        The alias e-mail

        :return: The email_address of this CreateAliasRequest.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CreateAliasRequest.

        The alias e-mail

        :param email_address: The email_address of this CreateAliasRequest.
        :type email_address: str
        """

        self._email_address = email_address
