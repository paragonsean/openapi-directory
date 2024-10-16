# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OnlineSettingsUpdateModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, book_ahead_unit: int=None, book_ahead_value: int=None, book_in_advance: int=None, booking_timer_mins: int=None, customer_bookings_per_day: int=None, enable_world_timezones: bool=None):
        """OnlineSettingsUpdateModel - a model defined in OpenAPI

        :param book_ahead_unit: The book_ahead_unit of this OnlineSettingsUpdateModel.
        :param book_ahead_value: The book_ahead_value of this OnlineSettingsUpdateModel.
        :param book_in_advance: The book_in_advance of this OnlineSettingsUpdateModel.
        :param booking_timer_mins: The booking_timer_mins of this OnlineSettingsUpdateModel.
        :param customer_bookings_per_day: The customer_bookings_per_day of this OnlineSettingsUpdateModel.
        :param enable_world_timezones: The enable_world_timezones of this OnlineSettingsUpdateModel.
        """
        self.openapi_types = {
            'book_ahead_unit': int,
            'book_ahead_value': int,
            'book_in_advance': int,
            'booking_timer_mins': int,
            'customer_bookings_per_day': int,
            'enable_world_timezones': bool
        }

        self.attribute_map = {
            'book_ahead_unit': 'bookAheadUnit',
            'book_ahead_value': 'bookAheadValue',
            'book_in_advance': 'bookInAdvance',
            'booking_timer_mins': 'bookingTimerMins',
            'customer_bookings_per_day': 'customerBookingsPerDay',
            'enable_world_timezones': 'enableWorldTimezones'
        }

        self._book_ahead_unit = book_ahead_unit
        self._book_ahead_value = book_ahead_value
        self._book_in_advance = book_in_advance
        self._booking_timer_mins = booking_timer_mins
        self._customer_bookings_per_day = customer_bookings_per_day
        self._enable_world_timezones = enable_world_timezones

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OnlineSettingsUpdateModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OnlineSettingsUpdateModel of this OnlineSettingsUpdateModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def book_ahead_unit(self):
        """Gets the book_ahead_unit of this OnlineSettingsUpdateModel.


        :return: The book_ahead_unit of this OnlineSettingsUpdateModel.
        :rtype: int
        """
        return self._book_ahead_unit

    @book_ahead_unit.setter
    def book_ahead_unit(self, book_ahead_unit):
        """Sets the book_ahead_unit of this OnlineSettingsUpdateModel.


        :param book_ahead_unit: The book_ahead_unit of this OnlineSettingsUpdateModel.
        :type book_ahead_unit: int
        """

        self._book_ahead_unit = book_ahead_unit

    @property
    def book_ahead_value(self):
        """Gets the book_ahead_value of this OnlineSettingsUpdateModel.


        :return: The book_ahead_value of this OnlineSettingsUpdateModel.
        :rtype: int
        """
        return self._book_ahead_value

    @book_ahead_value.setter
    def book_ahead_value(self, book_ahead_value):
        """Sets the book_ahead_value of this OnlineSettingsUpdateModel.


        :param book_ahead_value: The book_ahead_value of this OnlineSettingsUpdateModel.
        :type book_ahead_value: int
        """

        self._book_ahead_value = book_ahead_value

    @property
    def book_in_advance(self):
        """Gets the book_in_advance of this OnlineSettingsUpdateModel.


        :return: The book_in_advance of this OnlineSettingsUpdateModel.
        :rtype: int
        """
        return self._book_in_advance

    @book_in_advance.setter
    def book_in_advance(self, book_in_advance):
        """Sets the book_in_advance of this OnlineSettingsUpdateModel.


        :param book_in_advance: The book_in_advance of this OnlineSettingsUpdateModel.
        :type book_in_advance: int
        """

        self._book_in_advance = book_in_advance

    @property
    def booking_timer_mins(self):
        """Gets the booking_timer_mins of this OnlineSettingsUpdateModel.


        :return: The booking_timer_mins of this OnlineSettingsUpdateModel.
        :rtype: int
        """
        return self._booking_timer_mins

    @booking_timer_mins.setter
    def booking_timer_mins(self, booking_timer_mins):
        """Sets the booking_timer_mins of this OnlineSettingsUpdateModel.


        :param booking_timer_mins: The booking_timer_mins of this OnlineSettingsUpdateModel.
        :type booking_timer_mins: int
        """

        self._booking_timer_mins = booking_timer_mins

    @property
    def customer_bookings_per_day(self):
        """Gets the customer_bookings_per_day of this OnlineSettingsUpdateModel.


        :return: The customer_bookings_per_day of this OnlineSettingsUpdateModel.
        :rtype: int
        """
        return self._customer_bookings_per_day

    @customer_bookings_per_day.setter
    def customer_bookings_per_day(self, customer_bookings_per_day):
        """Sets the customer_bookings_per_day of this OnlineSettingsUpdateModel.


        :param customer_bookings_per_day: The customer_bookings_per_day of this OnlineSettingsUpdateModel.
        :type customer_bookings_per_day: int
        """

        self._customer_bookings_per_day = customer_bookings_per_day

    @property
    def enable_world_timezones(self):
        """Gets the enable_world_timezones of this OnlineSettingsUpdateModel.


        :return: The enable_world_timezones of this OnlineSettingsUpdateModel.
        :rtype: bool
        """
        return self._enable_world_timezones

    @enable_world_timezones.setter
    def enable_world_timezones(self, enable_world_timezones):
        """Sets the enable_world_timezones of this OnlineSettingsUpdateModel.


        :param enable_world_timezones: The enable_world_timezones of this OnlineSettingsUpdateModel.
        :type enable_world_timezones: bool
        """

        self._enable_world_timezones = enable_world_timezones
