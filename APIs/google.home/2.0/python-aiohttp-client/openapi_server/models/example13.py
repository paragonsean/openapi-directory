# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Example13(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, can_enroll: bool=None, enrollment_state: int=None, error_code: int=None, ready: bool=None, retryable: bool=None):
        """Example13 - a model defined in OpenAPI

        :param can_enroll: The can_enroll of this Example13.
        :param enrollment_state: The enrollment_state of this Example13.
        :param error_code: The error_code of this Example13.
        :param ready: The ready of this Example13.
        :param retryable: The retryable of this Example13.
        """
        self.openapi_types = {
            'can_enroll': bool,
            'enrollment_state': int,
            'error_code': int,
            'ready': bool,
            'retryable': bool
        }

        self.attribute_map = {
            'can_enroll': 'can_enroll',
            'enrollment_state': 'enrollment_state',
            'error_code': 'error_code',
            'ready': 'ready',
            'retryable': 'retryable'
        }

        self._can_enroll = can_enroll
        self._enrollment_state = enrollment_state
        self._error_code = error_code
        self._ready = ready
        self._retryable = retryable

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Example13':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Example13 of this Example13.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def can_enroll(self):
        """Gets the can_enroll of this Example13.


        :return: The can_enroll of this Example13.
        :rtype: bool
        """
        return self._can_enroll

    @can_enroll.setter
    def can_enroll(self, can_enroll):
        """Sets the can_enroll of this Example13.


        :param can_enroll: The can_enroll of this Example13.
        :type can_enroll: bool
        """
        if can_enroll is None:
            raise ValueError("Invalid value for `can_enroll`, must not be `None`")

        self._can_enroll = can_enroll

    @property
    def enrollment_state(self):
        """Gets the enrollment_state of this Example13.


        :return: The enrollment_state of this Example13.
        :rtype: int
        """
        return self._enrollment_state

    @enrollment_state.setter
    def enrollment_state(self, enrollment_state):
        """Sets the enrollment_state of this Example13.


        :param enrollment_state: The enrollment_state of this Example13.
        :type enrollment_state: int
        """
        if enrollment_state is None:
            raise ValueError("Invalid value for `enrollment_state`, must not be `None`")

        self._enrollment_state = enrollment_state

    @property
    def error_code(self):
        """Gets the error_code of this Example13.


        :return: The error_code of this Example13.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this Example13.


        :param error_code: The error_code of this Example13.
        :type error_code: int
        """
        if error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")

        self._error_code = error_code

    @property
    def ready(self):
        """Gets the ready of this Example13.


        :return: The ready of this Example13.
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this Example13.


        :param ready: The ready of this Example13.
        :type ready: bool
        """
        if ready is None:
            raise ValueError("Invalid value for `ready`, must not be `None`")

        self._ready = ready

    @property
    def retryable(self):
        """Gets the retryable of this Example13.


        :return: The retryable of this Example13.
        :rtype: bool
        """
        return self._retryable

    @retryable.setter
    def retryable(self, retryable):
        """Sets the retryable of this Example13.


        :param retryable: The retryable of this Example13.
        :type retryable: bool
        """
        if retryable is None:
            raise ValueError("Invalid value for `retryable`, must not be `None`")

        self._retryable = retryable
