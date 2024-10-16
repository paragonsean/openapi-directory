# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class APIModelsTokenOptions(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bearer_action: str=None, mac_action: str=None):
        """APIModelsTokenOptions - a model defined in OpenAPI

        :param bearer_action: The bearer_action of this APIModelsTokenOptions.
        :param mac_action: The mac_action of this APIModelsTokenOptions.
        """
        self.openapi_types = {
            'bearer_action': str,
            'mac_action': str
        }

        self.attribute_map = {
            'bearer_action': 'BearerAction',
            'mac_action': 'MACAction'
        }

        self._bearer_action = bearer_action
        self._mac_action = mac_action

    @classmethod
    def from_dict(cls, dikt: dict) -> 'APIModelsTokenOptions':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The API.Models.TokenOptions of this APIModelsTokenOptions.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bearer_action(self):
        """Gets the bearer_action of this APIModelsTokenOptions.

        The action to perform on the bearer token. Optional. Defaults to ‘None’.

        :return: The bearer_action of this APIModelsTokenOptions.
        :rtype: str
        """
        return self._bearer_action

    @bearer_action.setter
    def bearer_action(self, bearer_action):
        """Sets the bearer_action of this APIModelsTokenOptions.

        The action to perform on the bearer token. Optional. Defaults to ‘None’.

        :param bearer_action: The bearer_action of this APIModelsTokenOptions.
        :type bearer_action: str
        """
        allowed_values = ["None", "Reset", "Disable"]  # noqa: E501
        if bearer_action not in allowed_values:
            raise ValueError(
                "Invalid value for `bearer_action` ({0}), must be one of {1}"
                .format(bearer_action, allowed_values)
            )

        self._bearer_action = bearer_action

    @property
    def mac_action(self):
        """Gets the mac_action of this APIModelsTokenOptions.

        The action to perform on the MAC token. Optional. Defaults to ‘None’.

        :return: The mac_action of this APIModelsTokenOptions.
        :rtype: str
        """
        return self._mac_action

    @mac_action.setter
    def mac_action(self, mac_action):
        """Sets the mac_action of this APIModelsTokenOptions.

        The action to perform on the MAC token. Optional. Defaults to ‘None’.

        :param mac_action: The mac_action of this APIModelsTokenOptions.
        :type mac_action: str
        """
        allowed_values = ["None", "Reset", "Disable"]  # noqa: E501
        if mac_action not in allowed_values:
            raise ValueError(
                "Invalid value for `mac_action` ({0}), must be one of {1}"
                .format(mac_action, allowed_values)
            )

        self._mac_action = mac_action
