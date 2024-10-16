# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ErrorGroupState(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, annotation: str=None, state: str=None):
        """ErrorGroupState - a model defined in OpenAPI

        :param annotation: The annotation of this ErrorGroupState.
        :param state: The state of this ErrorGroupState.
        """
        self.openapi_types = {
            'annotation': str,
            'state': str
        }

        self.attribute_map = {
            'annotation': 'annotation',
            'state': 'state'
        }

        self._annotation = annotation
        self._state = state

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ErrorGroupState':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ErrorGroupState of this ErrorGroupState.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def annotation(self):
        """Gets the annotation of this ErrorGroupState.


        :return: The annotation of this ErrorGroupState.
        :rtype: str
        """
        return self._annotation

    @annotation.setter
    def annotation(self, annotation):
        """Sets the annotation of this ErrorGroupState.


        :param annotation: The annotation of this ErrorGroupState.
        :type annotation: str
        """

        self._annotation = annotation

    @property
    def state(self):
        """Gets the state of this ErrorGroupState.


        :return: The state of this ErrorGroupState.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ErrorGroupState.


        :param state: The state of this ErrorGroupState.
        :type state: str
        """
        allowed_values = ["open", "closed", "ignored"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state
