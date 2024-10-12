# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Schedule1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, state: str=None):
        """Schedule1 - a model defined in OpenAPI

        :param state: The state of this Schedule1.
        """
        self.openapi_types = {
            'state': str
        }

        self.attribute_map = {
            'state': 'state'
        }

        self._state = state

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Schedule1':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The schedule_1 of this Schedule1.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self):
        """Gets the state of this Schedule1.

        A schedule must be <strong>enabled</strong> to run. Specify <strong>enabled</strong> to run the schedule or <strong>disabled</strong> to turn off the schedule so that it doesn't run.

        :return: The state of this Schedule1.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Schedule1.

        A schedule must be <strong>enabled</strong> to run. Specify <strong>enabled</strong> to run the schedule or <strong>disabled</strong> to turn off the schedule so that it doesn't run.

        :param state: The state of this Schedule1.
        :type state: str
        """
        allowed_values = ["enabled", "disabled", "expired"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state
