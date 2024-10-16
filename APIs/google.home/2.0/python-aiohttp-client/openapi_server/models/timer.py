# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Timer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fire_time: int=None, id: str=None, original_duration: int=None, status: int=None):
        """Timer - a model defined in OpenAPI

        :param fire_time: The fire_time of this Timer.
        :param id: The id of this Timer.
        :param original_duration: The original_duration of this Timer.
        :param status: The status of this Timer.
        """
        self.openapi_types = {
            'fire_time': int,
            'id': str,
            'original_duration': int,
            'status': int
        }

        self.attribute_map = {
            'fire_time': 'fire_time',
            'id': 'id',
            'original_duration': 'original_duration',
            'status': 'status'
        }

        self._fire_time = fire_time
        self._id = id
        self._original_duration = original_duration
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Timer':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Timer of this Timer.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fire_time(self):
        """Gets the fire_time of this Timer.


        :return: The fire_time of this Timer.
        :rtype: int
        """
        return self._fire_time

    @fire_time.setter
    def fire_time(self, fire_time):
        """Sets the fire_time of this Timer.


        :param fire_time: The fire_time of this Timer.
        :type fire_time: int
        """
        if fire_time is None:
            raise ValueError("Invalid value for `fire_time`, must not be `None`")

        self._fire_time = fire_time

    @property
    def id(self):
        """Gets the id of this Timer.


        :return: The id of this Timer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Timer.


        :param id: The id of this Timer.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def original_duration(self):
        """Gets the original_duration of this Timer.


        :return: The original_duration of this Timer.
        :rtype: int
        """
        return self._original_duration

    @original_duration.setter
    def original_duration(self, original_duration):
        """Sets the original_duration of this Timer.


        :param original_duration: The original_duration of this Timer.
        :type original_duration: int
        """
        if original_duration is None:
            raise ValueError("Invalid value for `original_duration`, must not be `None`")

        self._original_duration = original_duration

    @property
    def status(self):
        """Gets the status of this Timer.


        :return: The status of this Timer.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Timer.


        :param status: The status of this Timer.
        :type status: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status
