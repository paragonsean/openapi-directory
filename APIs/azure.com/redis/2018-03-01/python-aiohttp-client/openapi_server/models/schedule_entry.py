# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ScheduleEntry(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, day_of_week: str=None, maintenance_window: str=None, start_hour_utc: int=None):
        """ScheduleEntry - a model defined in OpenAPI

        :param day_of_week: The day_of_week of this ScheduleEntry.
        :param maintenance_window: The maintenance_window of this ScheduleEntry.
        :param start_hour_utc: The start_hour_utc of this ScheduleEntry.
        """
        self.openapi_types = {
            'day_of_week': str,
            'maintenance_window': str,
            'start_hour_utc': int
        }

        self.attribute_map = {
            'day_of_week': 'dayOfWeek',
            'maintenance_window': 'maintenanceWindow',
            'start_hour_utc': 'startHourUtc'
        }

        self._day_of_week = day_of_week
        self._maintenance_window = maintenance_window
        self._start_hour_utc = start_hour_utc

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ScheduleEntry':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ScheduleEntry of this ScheduleEntry.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def day_of_week(self):
        """Gets the day_of_week of this ScheduleEntry.

        Day of the week when a cache can be patched.

        :return: The day_of_week of this ScheduleEntry.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this ScheduleEntry.

        Day of the week when a cache can be patched.

        :param day_of_week: The day_of_week of this ScheduleEntry.
        :type day_of_week: str
        """
        allowed_values = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Everyday", "Weekend"]  # noqa: E501
        if day_of_week not in allowed_values:
            raise ValueError(
                "Invalid value for `day_of_week` ({0}), must be one of {1}"
                .format(day_of_week, allowed_values)
            )

        self._day_of_week = day_of_week

    @property
    def maintenance_window(self):
        """Gets the maintenance_window of this ScheduleEntry.

        ISO8601 timespan specifying how much time cache patching can take. 

        :return: The maintenance_window of this ScheduleEntry.
        :rtype: str
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """Sets the maintenance_window of this ScheduleEntry.

        ISO8601 timespan specifying how much time cache patching can take. 

        :param maintenance_window: The maintenance_window of this ScheduleEntry.
        :type maintenance_window: str
        """

        self._maintenance_window = maintenance_window

    @property
    def start_hour_utc(self):
        """Gets the start_hour_utc of this ScheduleEntry.

        Start hour after which cache patching can start.

        :return: The start_hour_utc of this ScheduleEntry.
        :rtype: int
        """
        return self._start_hour_utc

    @start_hour_utc.setter
    def start_hour_utc(self, start_hour_utc):
        """Sets the start_hour_utc of this ScheduleEntry.

        Start hour after which cache patching can start.

        :param start_hour_utc: The start_hour_utc of this ScheduleEntry.
        :type start_hour_utc: int
        """
        if start_hour_utc is None:
            raise ValueError("Invalid value for `start_hour_utc`, must not be `None`")

        self._start_hour_utc = start_hour_utc
