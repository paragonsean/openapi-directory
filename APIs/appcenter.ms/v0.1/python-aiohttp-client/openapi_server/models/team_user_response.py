# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TeamUserResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, display_name: str=None, email: str=None, name: str=None, role: str=None):
        """TeamUserResponse - a model defined in OpenAPI

        :param display_name: The display_name of this TeamUserResponse.
        :param email: The email of this TeamUserResponse.
        :param name: The name of this TeamUserResponse.
        :param role: The role of this TeamUserResponse.
        """
        self.openapi_types = {
            'display_name': str,
            'email': str,
            'name': str,
            'role': str
        }

        self.attribute_map = {
            'display_name': 'display_name',
            'email': 'email',
            'name': 'name',
            'role': 'role'
        }

        self._display_name = display_name
        self._email = email
        self._name = name
        self._role = role

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TeamUserResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TeamUserResponse of this TeamUserResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def display_name(self):
        """Gets the display_name of this TeamUserResponse.

        The full name of the user. Might for example be first and last name

        :return: The display_name of this TeamUserResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TeamUserResponse.

        The full name of the user. Might for example be first and last name

        :param display_name: The display_name of this TeamUserResponse.
        :type display_name: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")

        self._display_name = display_name

    @property
    def email(self):
        """Gets the email of this TeamUserResponse.

        The email address of the user

        :return: The email of this TeamUserResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TeamUserResponse.

        The email address of the user

        :param email: The email of this TeamUserResponse.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def name(self):
        """Gets the name of this TeamUserResponse.

        The unique name that is used to identify the user.

        :return: The name of this TeamUserResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TeamUserResponse.

        The unique name that is used to identify the user.

        :param name: The name of this TeamUserResponse.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def role(self):
        """Gets the role of this TeamUserResponse.

        The role of the user has within the team

        :return: The role of this TeamUserResponse.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this TeamUserResponse.

        The role of the user has within the team

        :param role: The role of this TeamUserResponse.
        :type role: str
        """
        allowed_values = ["maintainer", "collaborator"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role
