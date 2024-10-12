# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OutputDateInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, day_of_week: float=None, day_of_year: float=None, minutes_in_day: float=None, seconds_in_day: float=None, ticks: float=None, week_of_year: float=None):
        """OutputDateInfo - a model defined in OpenAPI

        :param day_of_week: The day_of_week of this OutputDateInfo.
        :param day_of_year: The day_of_year of this OutputDateInfo.
        :param minutes_in_day: The minutes_in_day of this OutputDateInfo.
        :param seconds_in_day: The seconds_in_day of this OutputDateInfo.
        :param ticks: The ticks of this OutputDateInfo.
        :param week_of_year: The week_of_year of this OutputDateInfo.
        """
        self.openapi_types = {
            'day_of_week': float,
            'day_of_year': float,
            'minutes_in_day': float,
            'seconds_in_day': float,
            'ticks': float,
            'week_of_year': float
        }

        self.attribute_map = {
            'day_of_week': 'DayOfWeek',
            'day_of_year': 'DayOfYear',
            'minutes_in_day': 'MinutesInDay',
            'seconds_in_day': 'SecondsInDay',
            'ticks': 'Ticks',
            'week_of_year': 'WeekOfYear'
        }

        self._day_of_week = day_of_week
        self._day_of_year = day_of_year
        self._minutes_in_day = minutes_in_day
        self._seconds_in_day = seconds_in_day
        self._ticks = ticks
        self._week_of_year = week_of_year

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OutputDateInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The outputDateInfo of this OutputDateInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def day_of_week(self):
        """Gets the day_of_week of this OutputDateInfo.

        DayOfWeek

        :return: The day_of_week of this OutputDateInfo.
        :rtype: float
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this OutputDateInfo.

        DayOfWeek

        :param day_of_week: The day_of_week of this OutputDateInfo.
        :type day_of_week: float
        """

        self._day_of_week = day_of_week

    @property
    def day_of_year(self):
        """Gets the day_of_year of this OutputDateInfo.

        DayOfYear

        :return: The day_of_year of this OutputDateInfo.
        :rtype: float
        """
        return self._day_of_year

    @day_of_year.setter
    def day_of_year(self, day_of_year):
        """Sets the day_of_year of this OutputDateInfo.

        DayOfYear

        :param day_of_year: The day_of_year of this OutputDateInfo.
        :type day_of_year: float
        """

        self._day_of_year = day_of_year

    @property
    def minutes_in_day(self):
        """Gets the minutes_in_day of this OutputDateInfo.

        MinutesInDay

        :return: The minutes_in_day of this OutputDateInfo.
        :rtype: float
        """
        return self._minutes_in_day

    @minutes_in_day.setter
    def minutes_in_day(self, minutes_in_day):
        """Sets the minutes_in_day of this OutputDateInfo.

        MinutesInDay

        :param minutes_in_day: The minutes_in_day of this OutputDateInfo.
        :type minutes_in_day: float
        """

        self._minutes_in_day = minutes_in_day

    @property
    def seconds_in_day(self):
        """Gets the seconds_in_day of this OutputDateInfo.

        SecondsInDay

        :return: The seconds_in_day of this OutputDateInfo.
        :rtype: float
        """
        return self._seconds_in_day

    @seconds_in_day.setter
    def seconds_in_day(self, seconds_in_day):
        """Sets the seconds_in_day of this OutputDateInfo.

        SecondsInDay

        :param seconds_in_day: The seconds_in_day of this OutputDateInfo.
        :type seconds_in_day: float
        """

        self._seconds_in_day = seconds_in_day

    @property
    def ticks(self):
        """Gets the ticks of this OutputDateInfo.

        Ticks

        :return: The ticks of this OutputDateInfo.
        :rtype: float
        """
        return self._ticks

    @ticks.setter
    def ticks(self, ticks):
        """Sets the ticks of this OutputDateInfo.

        Ticks

        :param ticks: The ticks of this OutputDateInfo.
        :type ticks: float
        """

        self._ticks = ticks

    @property
    def week_of_year(self):
        """Gets the week_of_year of this OutputDateInfo.

        WeekOfYear

        :return: The week_of_year of this OutputDateInfo.
        :rtype: float
        """
        return self._week_of_year

    @week_of_year.setter
    def week_of_year(self, week_of_year):
        """Sets the week_of_year of this OutputDateInfo.

        WeekOfYear

        :param week_of_year: The week_of_year of this OutputDateInfo.
        :type week_of_year: float
        """

        self._week_of_year = week_of_year
