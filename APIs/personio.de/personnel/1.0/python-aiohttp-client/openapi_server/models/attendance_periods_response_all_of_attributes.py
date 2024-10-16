# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class AttendancePeriodsResponseAllOfAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _break: int=None, comment: str=None, _date: date=None, employee: int=None, end_time: str=None, is_holiday: bool=None, is_on_time_off: bool=None, start_time: str=None):
        """AttendancePeriodsResponseAllOfAttributes - a model defined in OpenAPI

        :param _break: The _break of this AttendancePeriodsResponseAllOfAttributes.
        :param comment: The comment of this AttendancePeriodsResponseAllOfAttributes.
        :param _date: The _date of this AttendancePeriodsResponseAllOfAttributes.
        :param employee: The employee of this AttendancePeriodsResponseAllOfAttributes.
        :param end_time: The end_time of this AttendancePeriodsResponseAllOfAttributes.
        :param is_holiday: The is_holiday of this AttendancePeriodsResponseAllOfAttributes.
        :param is_on_time_off: The is_on_time_off of this AttendancePeriodsResponseAllOfAttributes.
        :param start_time: The start_time of this AttendancePeriodsResponseAllOfAttributes.
        """
        self.openapi_types = {
            '_break': int,
            'comment': str,
            '_date': date,
            'employee': int,
            'end_time': str,
            'is_holiday': bool,
            'is_on_time_off': bool,
            'start_time': str
        }

        self.attribute_map = {
            '_break': 'break',
            'comment': 'comment',
            '_date': 'date',
            'employee': 'employee',
            'end_time': 'end_time',
            'is_holiday': 'is_holiday',
            'is_on_time_off': 'is_on_time_off',
            'start_time': 'start_time'
        }

        self.__break = _break
        self._comment = comment
        self.__date = _date
        self._employee = employee
        self._end_time = end_time
        self._is_holiday = is_holiday
        self._is_on_time_off = is_on_time_off
        self._start_time = start_time

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AttendancePeriodsResponseAllOfAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AttendancePeriodsResponse_allOf_attributes of this AttendancePeriodsResponseAllOfAttributes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _break(self):
        """Gets the _break of this AttendancePeriodsResponseAllOfAttributes.


        :return: The _break of this AttendancePeriodsResponseAllOfAttributes.
        :rtype: int
        """
        return self.__break

    @_break.setter
    def _break(self, _break):
        """Sets the _break of this AttendancePeriodsResponseAllOfAttributes.


        :param _break: The _break of this AttendancePeriodsResponseAllOfAttributes.
        :type _break: int
        """
        if _break is None:
            raise ValueError("Invalid value for `_break`, must not be `None`")

        self.__break = _break

    @property
    def comment(self):
        """Gets the comment of this AttendancePeriodsResponseAllOfAttributes.


        :return: The comment of this AttendancePeriodsResponseAllOfAttributes.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AttendancePeriodsResponseAllOfAttributes.


        :param comment: The comment of this AttendancePeriodsResponseAllOfAttributes.
        :type comment: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")

        self._comment = comment

    @property
    def _date(self):
        """Gets the _date of this AttendancePeriodsResponseAllOfAttributes.


        :return: The _date of this AttendancePeriodsResponseAllOfAttributes.
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this AttendancePeriodsResponseAllOfAttributes.


        :param _date: The _date of this AttendancePeriodsResponseAllOfAttributes.
        :type _date: date
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")

        self.__date = _date

    @property
    def employee(self):
        """Gets the employee of this AttendancePeriodsResponseAllOfAttributes.


        :return: The employee of this AttendancePeriodsResponseAllOfAttributes.
        :rtype: int
        """
        return self._employee

    @employee.setter
    def employee(self, employee):
        """Sets the employee of this AttendancePeriodsResponseAllOfAttributes.


        :param employee: The employee of this AttendancePeriodsResponseAllOfAttributes.
        :type employee: int
        """
        if employee is None:
            raise ValueError("Invalid value for `employee`, must not be `None`")

        self._employee = employee

    @property
    def end_time(self):
        """Gets the end_time of this AttendancePeriodsResponseAllOfAttributes.


        :return: The end_time of this AttendancePeriodsResponseAllOfAttributes.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AttendancePeriodsResponseAllOfAttributes.


        :param end_time: The end_time of this AttendancePeriodsResponseAllOfAttributes.
        :type end_time: str
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")
        if end_time is not None and not re.search(r'^\d\d:\d\d$', end_time):
            raise ValueError("Invalid value for `end_time`, must be a follow pattern or equal to `/^\d\d:\d\d$/`")

        self._end_time = end_time

    @property
    def is_holiday(self):
        """Gets the is_holiday of this AttendancePeriodsResponseAllOfAttributes.


        :return: The is_holiday of this AttendancePeriodsResponseAllOfAttributes.
        :rtype: bool
        """
        return self._is_holiday

    @is_holiday.setter
    def is_holiday(self, is_holiday):
        """Sets the is_holiday of this AttendancePeriodsResponseAllOfAttributes.


        :param is_holiday: The is_holiday of this AttendancePeriodsResponseAllOfAttributes.
        :type is_holiday: bool
        """
        if is_holiday is None:
            raise ValueError("Invalid value for `is_holiday`, must not be `None`")

        self._is_holiday = is_holiday

    @property
    def is_on_time_off(self):
        """Gets the is_on_time_off of this AttendancePeriodsResponseAllOfAttributes.


        :return: The is_on_time_off of this AttendancePeriodsResponseAllOfAttributes.
        :rtype: bool
        """
        return self._is_on_time_off

    @is_on_time_off.setter
    def is_on_time_off(self, is_on_time_off):
        """Sets the is_on_time_off of this AttendancePeriodsResponseAllOfAttributes.


        :param is_on_time_off: The is_on_time_off of this AttendancePeriodsResponseAllOfAttributes.
        :type is_on_time_off: bool
        """
        if is_on_time_off is None:
            raise ValueError("Invalid value for `is_on_time_off`, must not be `None`")

        self._is_on_time_off = is_on_time_off

    @property
    def start_time(self):
        """Gets the start_time of this AttendancePeriodsResponseAllOfAttributes.


        :return: The start_time of this AttendancePeriodsResponseAllOfAttributes.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AttendancePeriodsResponseAllOfAttributes.


        :param start_time: The start_time of this AttendancePeriodsResponseAllOfAttributes.
        :type start_time: str
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")
        if start_time is not None and not re.search(r'^\d\d:\d\d$', start_time):
            raise ValueError("Invalid value for `start_time`, must be a follow pattern or equal to `/^\d\d:\d\d$/`")

        self._start_time = start_time
