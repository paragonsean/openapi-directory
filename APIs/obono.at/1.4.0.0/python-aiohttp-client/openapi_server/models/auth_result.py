# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AuthResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access_token: str=None, registrierkasse_uuid: str=None):
        """AuthResult - a model defined in OpenAPI

        :param access_token: The access_token of this AuthResult.
        :param registrierkasse_uuid: The registrierkasse_uuid of this AuthResult.
        """
        self.openapi_types = {
            'access_token': str,
            'registrierkasse_uuid': str
        }

        self.attribute_map = {
            'access_token': 'accessToken',
            'registrierkasse_uuid': 'registrierkasseUuid'
        }

        self._access_token = access_token
        self._registrierkasse_uuid = registrierkasse_uuid

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AuthResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AuthResult of this AuthResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_token(self):
        """Gets the access_token of this AuthResult.


        :return: The access_token of this AuthResult.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this AuthResult.


        :param access_token: The access_token of this AuthResult.
        :type access_token: str
        """

        self._access_token = access_token

    @property
    def registrierkasse_uuid(self):
        """Gets the registrierkasse_uuid of this AuthResult.


        :return: The registrierkasse_uuid of this AuthResult.
        :rtype: str
        """
        return self._registrierkasse_uuid

    @registrierkasse_uuid.setter
    def registrierkasse_uuid(self, registrierkasse_uuid):
        """Sets the registrierkasse_uuid of this AuthResult.


        :param registrierkasse_uuid: The registrierkasse_uuid of this AuthResult.
        :type registrierkasse_uuid: str
        """

        self._registrierkasse_uuid = registrierkasse_uuid
