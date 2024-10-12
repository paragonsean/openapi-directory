# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateSessionRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, collaborator_user_id: str=None, host: str=None):
        """CreateSessionRequest - a model defined in OpenAPI

        :param collaborator_user_id: The collaborator_user_id of this CreateSessionRequest.
        :param host: The host of this CreateSessionRequest.
        """
        self.openapi_types = {
            'collaborator_user_id': str,
            'host': str
        }

        self.attribute_map = {
            'collaborator_user_id': 'collaboratorUserId',
            'host': 'host'
        }

        self._collaborator_user_id = collaborator_user_id
        self._host = host

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateSessionRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The create_session_request of this CreateSessionRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def collaborator_user_id(self):
        """Gets the collaborator_user_id of this CreateSessionRequest.


        :return: The collaborator_user_id of this CreateSessionRequest.
        :rtype: str
        """
        return self._collaborator_user_id

    @collaborator_user_id.setter
    def collaborator_user_id(self, collaborator_user_id):
        """Sets the collaborator_user_id of this CreateSessionRequest.


        :param collaborator_user_id: The collaborator_user_id of this CreateSessionRequest.
        :type collaborator_user_id: str
        """

        self._collaborator_user_id = collaborator_user_id

    @property
    def host(self):
        """Gets the host of this CreateSessionRequest.


        :return: The host of this CreateSessionRequest.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CreateSessionRequest.


        :param host: The host of this CreateSessionRequest.
        :type host: str
        """

        self._host = host
