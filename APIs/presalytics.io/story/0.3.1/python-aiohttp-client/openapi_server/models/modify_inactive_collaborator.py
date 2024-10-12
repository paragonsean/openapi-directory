# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ModifyInactiveCollaborator(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, action: str=None, lead_id: int=None, user_id: str=None):
        """ModifyInactiveCollaborator - a model defined in OpenAPI

        :param action: The action of this ModifyInactiveCollaborator.
        :param lead_id: The lead_id of this ModifyInactiveCollaborator.
        :param user_id: The user_id of this ModifyInactiveCollaborator.
        """
        self.openapi_types = {
            'action': str,
            'lead_id': int,
            'user_id': str
        }

        self.attribute_map = {
            'action': 'action',
            'lead_id': 'lead_id',
            'user_id': 'user_id'
        }

        self._action = action
        self._lead_id = lead_id
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ModifyInactiveCollaborator':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The modify_inactive_collaborator of this ModifyInactiveCollaborator.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action(self):
        """Gets the action of this ModifyInactiveCollaborator.


        :return: The action of this ModifyInactiveCollaborator.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ModifyInactiveCollaborator.


        :param action: The action of this ModifyInactiveCollaborator.
        :type action: str
        """

        self._action = action

    @property
    def lead_id(self):
        """Gets the lead_id of this ModifyInactiveCollaborator.


        :return: The lead_id of this ModifyInactiveCollaborator.
        :rtype: int
        """
        return self._lead_id

    @lead_id.setter
    def lead_id(self, lead_id):
        """Sets the lead_id of this ModifyInactiveCollaborator.


        :param lead_id: The lead_id of this ModifyInactiveCollaborator.
        :type lead_id: int
        """

        self._lead_id = lead_id

    @property
    def user_id(self):
        """Gets the user_id of this ModifyInactiveCollaborator.


        :return: The user_id of this ModifyInactiveCollaborator.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ModifyInactiveCollaborator.


        :param user_id: The user_id of this ModifyInactiveCollaborator.
        :type user_id: str
        """

        self._user_id = user_id
