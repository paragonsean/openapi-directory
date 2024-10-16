# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class APIModelsUserEffectivePermission(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, permission_id: int=None, permission_name: str=None, user_id: int=None):
        """APIModelsUserEffectivePermission - a model defined in OpenAPI

        :param permission_id: The permission_id of this APIModelsUserEffectivePermission.
        :param permission_name: The permission_name of this APIModelsUserEffectivePermission.
        :param user_id: The user_id of this APIModelsUserEffectivePermission.
        """
        self.openapi_types = {
            'permission_id': int,
            'permission_name': str,
            'user_id': int
        }

        self.attribute_map = {
            'permission_id': 'PermissionId',
            'permission_name': 'PermissionName',
            'user_id': 'UserID'
        }

        self._permission_id = permission_id
        self._permission_name = permission_name
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'APIModelsUserEffectivePermission':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The API.Models.UserEffectivePermission of this APIModelsUserEffectivePermission.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def permission_id(self):
        """Gets the permission_id of this APIModelsUserEffectivePermission.


        :return: The permission_id of this APIModelsUserEffectivePermission.
        :rtype: int
        """
        return self._permission_id

    @permission_id.setter
    def permission_id(self, permission_id):
        """Sets the permission_id of this APIModelsUserEffectivePermission.


        :param permission_id: The permission_id of this APIModelsUserEffectivePermission.
        :type permission_id: int
        """

        self._permission_id = permission_id

    @property
    def permission_name(self):
        """Gets the permission_name of this APIModelsUserEffectivePermission.


        :return: The permission_name of this APIModelsUserEffectivePermission.
        :rtype: str
        """
        return self._permission_name

    @permission_name.setter
    def permission_name(self, permission_name):
        """Sets the permission_name of this APIModelsUserEffectivePermission.


        :param permission_name: The permission_name of this APIModelsUserEffectivePermission.
        :type permission_name: str
        """

        self._permission_name = permission_name

    @property
    def user_id(self):
        """Gets the user_id of this APIModelsUserEffectivePermission.


        :return: The user_id of this APIModelsUserEffectivePermission.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this APIModelsUserEffectivePermission.


        :param user_id: The user_id of this APIModelsUserEffectivePermission.
        :type user_id: int
        """

        self._user_id = user_id
