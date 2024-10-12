# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ProjectCollaboratorInvite(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, comment: str=None, email: str=None, role_name: str=None, user_id: int=None):
        """ProjectCollaboratorInvite - a model defined in OpenAPI

        :param comment: The comment of this ProjectCollaboratorInvite.
        :param email: The email of this ProjectCollaboratorInvite.
        :param role_name: The role_name of this ProjectCollaboratorInvite.
        :param user_id: The user_id of this ProjectCollaboratorInvite.
        """
        self.openapi_types = {
            'comment': str,
            'email': str,
            'role_name': str,
            'user_id': int
        }

        self.attribute_map = {
            'comment': 'comment',
            'email': 'email',
            'role_name': 'role_name',
            'user_id': 'user_id'
        }

        self._comment = comment
        self._email = email
        self._role_name = role_name
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProjectCollaboratorInvite':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ProjectCollaboratorInvite of this ProjectCollaboratorInvite.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def comment(self):
        """Gets the comment of this ProjectCollaboratorInvite.

        Text sent when inviting the user to the project

        :return: The comment of this ProjectCollaboratorInvite.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ProjectCollaboratorInvite.

        Text sent when inviting the user to the project

        :param comment: The comment of this ProjectCollaboratorInvite.
        :type comment: str
        """

        self._comment = comment

    @property
    def email(self):
        """Gets the email of this ProjectCollaboratorInvite.

        Collaborator email

        :return: The email of this ProjectCollaboratorInvite.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ProjectCollaboratorInvite.

        Collaborator email

        :param email: The email of this ProjectCollaboratorInvite.
        :type email: str
        """

        self._email = email

    @property
    def role_name(self):
        """Gets the role_name of this ProjectCollaboratorInvite.

        Role of the the collaborator inside the project

        :return: The role_name of this ProjectCollaboratorInvite.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this ProjectCollaboratorInvite.

        Role of the the collaborator inside the project

        :param role_name: The role_name of this ProjectCollaboratorInvite.
        :type role_name: str
        """
        allowed_values = ["viewer", "collaborator"]  # noqa: E501
        if role_name not in allowed_values:
            raise ValueError(
                "Invalid value for `role_name` ({0}), must be one of {1}"
                .format(role_name, allowed_values)
            )

        self._role_name = role_name

    @property
    def user_id(self):
        """Gets the user_id of this ProjectCollaboratorInvite.

        User id of the collaborator

        :return: The user_id of this ProjectCollaboratorInvite.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ProjectCollaboratorInvite.

        User id of the collaborator

        :param user_id: The user_id of this ProjectCollaboratorInvite.
        :type user_id: int
        """

        self._user_id = user_id
