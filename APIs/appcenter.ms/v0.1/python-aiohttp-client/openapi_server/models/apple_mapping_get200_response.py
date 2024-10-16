# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AppleMappingGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_id: str=None, apple_id: str=None, service_connection_id: str=None, team_identifier: str=None):
        """AppleMappingGet200Response - a model defined in OpenAPI

        :param app_id: The app_id of this AppleMappingGet200Response.
        :param apple_id: The apple_id of this AppleMappingGet200Response.
        :param service_connection_id: The service_connection_id of this AppleMappingGet200Response.
        :param team_identifier: The team_identifier of this AppleMappingGet200Response.
        """
        self.openapi_types = {
            'app_id': str,
            'apple_id': str,
            'service_connection_id': str,
            'team_identifier': str
        }

        self.attribute_map = {
            'app_id': 'app_id',
            'apple_id': 'apple_id',
            'service_connection_id': 'service_connection_id',
            'team_identifier': 'team_identifier'
        }

        self._app_id = app_id
        self._apple_id = apple_id
        self._service_connection_id = service_connection_id
        self._team_identifier = team_identifier

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AppleMappingGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The appleMapping_get_200_response of this AppleMappingGet200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_id(self):
        """Gets the app_id of this AppleMappingGet200Response.

        ID of the apple application in Mobile Center

        :return: The app_id of this AppleMappingGet200Response.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AppleMappingGet200Response.

        ID of the apple application in Mobile Center

        :param app_id: The app_id of this AppleMappingGet200Response.
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def apple_id(self):
        """Gets the apple_id of this AppleMappingGet200Response.

        ID of the apple application in apple store

        :return: The apple_id of this AppleMappingGet200Response.
        :rtype: str
        """
        return self._apple_id

    @apple_id.setter
    def apple_id(self, apple_id):
        """Sets the apple_id of this AppleMappingGet200Response.

        ID of the apple application in apple store

        :param apple_id: The apple_id of this AppleMappingGet200Response.
        :type apple_id: str
        """

        self._apple_id = apple_id

    @property
    def service_connection_id(self):
        """Gets the service_connection_id of this AppleMappingGet200Response.

        Id for the shared service connection. In case of Apple AppStore, this connection will be used to create and connect to the Apple AppStore in Mobile Center.

        :return: The service_connection_id of this AppleMappingGet200Response.
        :rtype: str
        """
        return self._service_connection_id

    @service_connection_id.setter
    def service_connection_id(self, service_connection_id):
        """Sets the service_connection_id of this AppleMappingGet200Response.

        Id for the shared service connection. In case of Apple AppStore, this connection will be used to create and connect to the Apple AppStore in Mobile Center.

        :param service_connection_id: The service_connection_id of this AppleMappingGet200Response.
        :type service_connection_id: str
        """

        self._service_connection_id = service_connection_id

    @property
    def team_identifier(self):
        """Gets the team_identifier of this AppleMappingGet200Response.

        ID of the Team associated with the app in apple store

        :return: The team_identifier of this AppleMappingGet200Response.
        :rtype: str
        """
        return self._team_identifier

    @team_identifier.setter
    def team_identifier(self, team_identifier):
        """Sets the team_identifier of this AppleMappingGet200Response.

        ID of the Team associated with the app in apple store

        :param team_identifier: The team_identifier of this AppleMappingGet200Response.
        :type team_identifier: str
        """

        self._team_identifier = team_identifier
