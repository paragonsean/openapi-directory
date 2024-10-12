# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.sla_start_time_attributes import SlaStartTimeAttributes
from openapi_server import util


class BackupWindow(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, duration_in_hours: int=None, start_time_attributes: SlaStartTimeAttributes=None):
        """BackupWindow - a model defined in OpenAPI

        :param duration_in_hours: The duration_in_hours of this BackupWindow.
        :param start_time_attributes: The start_time_attributes of this BackupWindow.
        """
        self.openapi_types = {
            'duration_in_hours': int,
            'start_time_attributes': SlaStartTimeAttributes
        }

        self.attribute_map = {
            'duration_in_hours': 'durationInHours',
            'start_time_attributes': 'startTimeAttributes'
        }

        self._duration_in_hours = duration_in_hours
        self._start_time_attributes = start_time_attributes

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BackupWindow':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BackupWindow of this BackupWindow.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def duration_in_hours(self):
        """Gets the duration_in_hours of this BackupWindow.


        :return: The duration_in_hours of this BackupWindow.
        :rtype: int
        """
        return self._duration_in_hours

    @duration_in_hours.setter
    def duration_in_hours(self, duration_in_hours):
        """Sets the duration_in_hours of this BackupWindow.


        :param duration_in_hours: The duration_in_hours of this BackupWindow.
        :type duration_in_hours: int
        """
        if duration_in_hours is None:
            raise ValueError("Invalid value for `duration_in_hours`, must not be `None`")

        self._duration_in_hours = duration_in_hours

    @property
    def start_time_attributes(self):
        """Gets the start_time_attributes of this BackupWindow.


        :return: The start_time_attributes of this BackupWindow.
        :rtype: SlaStartTimeAttributes
        """
        return self._start_time_attributes

    @start_time_attributes.setter
    def start_time_attributes(self, start_time_attributes):
        """Sets the start_time_attributes of this BackupWindow.


        :param start_time_attributes: The start_time_attributes of this BackupWindow.
        :type start_time_attributes: SlaStartTimeAttributes
        """
        if start_time_attributes is None:
            raise ValueError("Invalid value for `start_time_attributes`, must not be `None`")

        self._start_time_attributes = start_time_attributes
