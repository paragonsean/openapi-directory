# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OutputDateDifference(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, days: float=None, hours: float=None, milliseconds: float=None, minutes: float=None, months: float=None, ticks: float=None, total_days: float=None, total_hours: float=None, total_milliseconds: float=None, total_minutes: float=None, total_months: float=None, total_seconds: float=None, total_years: float=None, years: float=None):
        """OutputDateDifference - a model defined in OpenAPI

        :param days: The days of this OutputDateDifference.
        :param hours: The hours of this OutputDateDifference.
        :param milliseconds: The milliseconds of this OutputDateDifference.
        :param minutes: The minutes of this OutputDateDifference.
        :param months: The months of this OutputDateDifference.
        :param ticks: The ticks of this OutputDateDifference.
        :param total_days: The total_days of this OutputDateDifference.
        :param total_hours: The total_hours of this OutputDateDifference.
        :param total_milliseconds: The total_milliseconds of this OutputDateDifference.
        :param total_minutes: The total_minutes of this OutputDateDifference.
        :param total_months: The total_months of this OutputDateDifference.
        :param total_seconds: The total_seconds of this OutputDateDifference.
        :param total_years: The total_years of this OutputDateDifference.
        :param years: The years of this OutputDateDifference.
        """
        self.openapi_types = {
            'days': float,
            'hours': float,
            'milliseconds': float,
            'minutes': float,
            'months': float,
            'ticks': float,
            'total_days': float,
            'total_hours': float,
            'total_milliseconds': float,
            'total_minutes': float,
            'total_months': float,
            'total_seconds': float,
            'total_years': float,
            'years': float
        }

        self.attribute_map = {
            'days': 'days',
            'hours': 'hours',
            'milliseconds': 'milliseconds',
            'minutes': 'minutes',
            'months': 'months',
            'ticks': 'ticks',
            'total_days': 'totalDays',
            'total_hours': 'totalHours',
            'total_milliseconds': 'totalMilliseconds',
            'total_minutes': 'totalMinutes',
            'total_months': 'totalMonths',
            'total_seconds': 'totalSeconds',
            'total_years': 'totalYears',
            'years': 'years'
        }

        self._days = days
        self._hours = hours
        self._milliseconds = milliseconds
        self._minutes = minutes
        self._months = months
        self._ticks = ticks
        self._total_days = total_days
        self._total_hours = total_hours
        self._total_milliseconds = total_milliseconds
        self._total_minutes = total_minutes
        self._total_months = total_months
        self._total_seconds = total_seconds
        self._total_years = total_years
        self._years = years

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OutputDateDifference':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The outputDateDifference of this OutputDateDifference.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def days(self):
        """Gets the days of this OutputDateDifference.

        Days

        :return: The days of this OutputDateDifference.
        :rtype: float
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this OutputDateDifference.

        Days

        :param days: The days of this OutputDateDifference.
        :type days: float
        """

        self._days = days

    @property
    def hours(self):
        """Gets the hours of this OutputDateDifference.

        Hours

        :return: The hours of this OutputDateDifference.
        :rtype: float
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this OutputDateDifference.

        Hours

        :param hours: The hours of this OutputDateDifference.
        :type hours: float
        """

        self._hours = hours

    @property
    def milliseconds(self):
        """Gets the milliseconds of this OutputDateDifference.

        Milliseconds

        :return: The milliseconds of this OutputDateDifference.
        :rtype: float
        """
        return self._milliseconds

    @milliseconds.setter
    def milliseconds(self, milliseconds):
        """Sets the milliseconds of this OutputDateDifference.

        Milliseconds

        :param milliseconds: The milliseconds of this OutputDateDifference.
        :type milliseconds: float
        """

        self._milliseconds = milliseconds

    @property
    def minutes(self):
        """Gets the minutes of this OutputDateDifference.

        Minutes

        :return: The minutes of this OutputDateDifference.
        :rtype: float
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this OutputDateDifference.

        Minutes

        :param minutes: The minutes of this OutputDateDifference.
        :type minutes: float
        """

        self._minutes = minutes

    @property
    def months(self):
        """Gets the months of this OutputDateDifference.

        Months

        :return: The months of this OutputDateDifference.
        :rtype: float
        """
        return self._months

    @months.setter
    def months(self, months):
        """Sets the months of this OutputDateDifference.

        Months

        :param months: The months of this OutputDateDifference.
        :type months: float
        """

        self._months = months

    @property
    def ticks(self):
        """Gets the ticks of this OutputDateDifference.

        Ticks

        :return: The ticks of this OutputDateDifference.
        :rtype: float
        """
        return self._ticks

    @ticks.setter
    def ticks(self, ticks):
        """Sets the ticks of this OutputDateDifference.

        Ticks

        :param ticks: The ticks of this OutputDateDifference.
        :type ticks: float
        """

        self._ticks = ticks

    @property
    def total_days(self):
        """Gets the total_days of this OutputDateDifference.

        Total Days

        :return: The total_days of this OutputDateDifference.
        :rtype: float
        """
        return self._total_days

    @total_days.setter
    def total_days(self, total_days):
        """Sets the total_days of this OutputDateDifference.

        Total Days

        :param total_days: The total_days of this OutputDateDifference.
        :type total_days: float
        """

        self._total_days = total_days

    @property
    def total_hours(self):
        """Gets the total_hours of this OutputDateDifference.

        Total Hours

        :return: The total_hours of this OutputDateDifference.
        :rtype: float
        """
        return self._total_hours

    @total_hours.setter
    def total_hours(self, total_hours):
        """Sets the total_hours of this OutputDateDifference.

        Total Hours

        :param total_hours: The total_hours of this OutputDateDifference.
        :type total_hours: float
        """

        self._total_hours = total_hours

    @property
    def total_milliseconds(self):
        """Gets the total_milliseconds of this OutputDateDifference.

        Total Milliseconds

        :return: The total_milliseconds of this OutputDateDifference.
        :rtype: float
        """
        return self._total_milliseconds

    @total_milliseconds.setter
    def total_milliseconds(self, total_milliseconds):
        """Sets the total_milliseconds of this OutputDateDifference.

        Total Milliseconds

        :param total_milliseconds: The total_milliseconds of this OutputDateDifference.
        :type total_milliseconds: float
        """

        self._total_milliseconds = total_milliseconds

    @property
    def total_minutes(self):
        """Gets the total_minutes of this OutputDateDifference.

        Total Minutes

        :return: The total_minutes of this OutputDateDifference.
        :rtype: float
        """
        return self._total_minutes

    @total_minutes.setter
    def total_minutes(self, total_minutes):
        """Sets the total_minutes of this OutputDateDifference.

        Total Minutes

        :param total_minutes: The total_minutes of this OutputDateDifference.
        :type total_minutes: float
        """

        self._total_minutes = total_minutes

    @property
    def total_months(self):
        """Gets the total_months of this OutputDateDifference.

        Total Months

        :return: The total_months of this OutputDateDifference.
        :rtype: float
        """
        return self._total_months

    @total_months.setter
    def total_months(self, total_months):
        """Sets the total_months of this OutputDateDifference.

        Total Months

        :param total_months: The total_months of this OutputDateDifference.
        :type total_months: float
        """

        self._total_months = total_months

    @property
    def total_seconds(self):
        """Gets the total_seconds of this OutputDateDifference.

        Total Seconds

        :return: The total_seconds of this OutputDateDifference.
        :rtype: float
        """
        return self._total_seconds

    @total_seconds.setter
    def total_seconds(self, total_seconds):
        """Sets the total_seconds of this OutputDateDifference.

        Total Seconds

        :param total_seconds: The total_seconds of this OutputDateDifference.
        :type total_seconds: float
        """

        self._total_seconds = total_seconds

    @property
    def total_years(self):
        """Gets the total_years of this OutputDateDifference.

        Total Years

        :return: The total_years of this OutputDateDifference.
        :rtype: float
        """
        return self._total_years

    @total_years.setter
    def total_years(self, total_years):
        """Sets the total_years of this OutputDateDifference.

        Total Years

        :param total_years: The total_years of this OutputDateDifference.
        :type total_years: float
        """

        self._total_years = total_years

    @property
    def years(self):
        """Gets the years of this OutputDateDifference.

        Years

        :return: The years of this OutputDateDifference.
        :rtype: float
        """
        return self._years

    @years.setter
    def years(self, years):
        """Sets the years of this OutputDateDifference.

        Years

        :param years: The years of this OutputDateDifference.
        :type years: float
        """

        self._years = years
