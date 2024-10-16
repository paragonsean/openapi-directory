# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AppResponseInternalAllOfUserPermissions(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, permissions: List[str]=None, user_id: str=None):
        """AppResponseInternalAllOfUserPermissions - a model defined in OpenAPI

        :param permissions: The permissions of this AppResponseInternalAllOfUserPermissions.
        :param user_id: The user_id of this AppResponseInternalAllOfUserPermissions.
        """
        self.openapi_types = {
            'permissions': List[str],
            'user_id': str
        }

        self.attribute_map = {
            'permissions': 'permissions',
            'user_id': 'user_id'
        }

        self._permissions = permissions
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AppResponseInternalAllOfUserPermissions':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AppResponseInternal_allOf_user_permissions of this AppResponseInternalAllOfUserPermissions.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def permissions(self):
        """Gets the permissions of this AppResponseInternalAllOfUserPermissions.


        :return: The permissions of this AppResponseInternalAllOfUserPermissions.
        :rtype: List[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this AppResponseInternalAllOfUserPermissions.


        :param permissions: The permissions of this AppResponseInternalAllOfUserPermissions.
        :type permissions: List[str]
        """
        allowed_values = ["manager", "developer", "viewer", "tester"]  # noqa: E501
        if not set(permissions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `permissions` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(permissions) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._permissions = permissions

    @property
    def user_id(self):
        """Gets the user_id of this AppResponseInternalAllOfUserPermissions.


        :return: The user_id of this AppResponseInternalAllOfUserPermissions.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AppResponseInternalAllOfUserPermissions.


        :param user_id: The user_id of this AppResponseInternalAllOfUserPermissions.
        :type user_id: str
        """

        self._user_id = user_id
