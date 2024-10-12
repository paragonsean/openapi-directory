# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Collaborator(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, role_name: str=None, user_id: int=None):
        """Collaborator - a model defined in OpenAPI

        :param name: The name of this Collaborator.
        :param role_name: The role_name of this Collaborator.
        :param user_id: The user_id of this Collaborator.
        """
        self.openapi_types = {
            'name': str,
            'role_name': str,
            'user_id': int
        }

        self.attribute_map = {
            'name': 'name',
            'role_name': 'role_name',
            'user_id': 'user_id'
        }

        self._name = name
        self._role_name = role_name
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Collaborator':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Collaborator of this Collaborator.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Collaborator.

        Collaborator name

        :return: The name of this Collaborator.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Collaborator.

        Collaborator name

        :param name: The name of this Collaborator.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def role_name(self):
        """Gets the role_name of this Collaborator.

        Collaborator role

        :return: The role_name of this Collaborator.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this Collaborator.

        Collaborator role

        :param role_name: The role_name of this Collaborator.
        :type role_name: str
        """
        if role_name is None:
            raise ValueError("Invalid value for `role_name`, must not be `None`")

        self._role_name = role_name

    @property
    def user_id(self):
        """Gets the user_id of this Collaborator.

        Collaborator id

        :return: The user_id of this Collaborator.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Collaborator.

        Collaborator id

        :param user_id: The user_id of this Collaborator.
        :type user_id: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")

        self._user_id = user_id
