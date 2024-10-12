# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ManageEvent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, action: str=None, action_params: Dict[str, object]=None, name: str=None):
        """ManageEvent - a model defined in OpenAPI

        :param action: The action of this ManageEvent.
        :param action_params: The action_params of this ManageEvent.
        :param name: The name of this ManageEvent.
        """
        self.openapi_types = {
            'action': str,
            'action_params': Dict[str, object],
            'name': str
        }

        self.attribute_map = {
            'action': 'action',
            'action_params': 'action_params',
            'name': 'name'
        }

        self._action = action
        self._action_params = action_params
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ManageEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The manage_event of this ManageEvent.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action(self):
        """Gets the action of this ManageEvent.


        :return: The action of this ManageEvent.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ManageEvent.


        :param action: The action of this ManageEvent.
        :type action: str
        """
        allowed_values = ["create", "fire", "change", "delete"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def action_params(self):
        """Gets the action_params of this ManageEvent.


        :return: The action_params of this ManageEvent.
        :rtype: Dict[str, object]
        """
        return self._action_params

    @action_params.setter
    def action_params(self, action_params):
        """Sets the action_params of this ManageEvent.


        :param action_params: The action_params of this ManageEvent.
        :type action_params: Dict[str, object]
        """

        self._action_params = action_params

    @property
    def name(self):
        """Gets the name of this ManageEvent.


        :return: The name of this ManageEvent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ManageEvent.


        :param name: The name of this ManageEvent.
        :type name: str
        """

        self._name = name
