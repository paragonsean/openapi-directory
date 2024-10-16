# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ResourceOptionsInputModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bio_link: str=None, booking_notification: int=None, calendar_availability: int=None, display_color: str=None, effective_date: datetime=None, gender: str=None, google_calendar_id: str=None, hourly: float=None, ignore_business_hours: bool=None, notification_type: int=None, outlook_calendar_id: str=None, sort_key: int=None):
        """ResourceOptionsInputModel - a model defined in OpenAPI

        :param bio_link: The bio_link of this ResourceOptionsInputModel.
        :param booking_notification: The booking_notification of this ResourceOptionsInputModel.
        :param calendar_availability: The calendar_availability of this ResourceOptionsInputModel.
        :param display_color: The display_color of this ResourceOptionsInputModel.
        :param effective_date: The effective_date of this ResourceOptionsInputModel.
        :param gender: The gender of this ResourceOptionsInputModel.
        :param google_calendar_id: The google_calendar_id of this ResourceOptionsInputModel.
        :param hourly: The hourly of this ResourceOptionsInputModel.
        :param ignore_business_hours: The ignore_business_hours of this ResourceOptionsInputModel.
        :param notification_type: The notification_type of this ResourceOptionsInputModel.
        :param outlook_calendar_id: The outlook_calendar_id of this ResourceOptionsInputModel.
        :param sort_key: The sort_key of this ResourceOptionsInputModel.
        """
        self.openapi_types = {
            'bio_link': str,
            'booking_notification': int,
            'calendar_availability': int,
            'display_color': str,
            'effective_date': datetime,
            'gender': str,
            'google_calendar_id': str,
            'hourly': float,
            'ignore_business_hours': bool,
            'notification_type': int,
            'outlook_calendar_id': str,
            'sort_key': int
        }

        self.attribute_map = {
            'bio_link': 'bioLink',
            'booking_notification': 'bookingNotification',
            'calendar_availability': 'calendarAvailability',
            'display_color': 'displayColor',
            'effective_date': 'effectiveDate',
            'gender': 'gender',
            'google_calendar_id': 'googleCalendarId',
            'hourly': 'hourly',
            'ignore_business_hours': 'ignoreBusinessHours',
            'notification_type': 'notificationType',
            'outlook_calendar_id': 'outlookCalendarId',
            'sort_key': 'sortKey'
        }

        self._bio_link = bio_link
        self._booking_notification = booking_notification
        self._calendar_availability = calendar_availability
        self._display_color = display_color
        self._effective_date = effective_date
        self._gender = gender
        self._google_calendar_id = google_calendar_id
        self._hourly = hourly
        self._ignore_business_hours = ignore_business_hours
        self._notification_type = notification_type
        self._outlook_calendar_id = outlook_calendar_id
        self._sort_key = sort_key

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ResourceOptionsInputModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ResourceOptionsInputModel of this ResourceOptionsInputModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bio_link(self):
        """Gets the bio_link of this ResourceOptionsInputModel.


        :return: The bio_link of this ResourceOptionsInputModel.
        :rtype: str
        """
        return self._bio_link

    @bio_link.setter
    def bio_link(self, bio_link):
        """Sets the bio_link of this ResourceOptionsInputModel.


        :param bio_link: The bio_link of this ResourceOptionsInputModel.
        :type bio_link: str
        """

        self._bio_link = bio_link

    @property
    def booking_notification(self):
        """Gets the booking_notification of this ResourceOptionsInputModel.


        :return: The booking_notification of this ResourceOptionsInputModel.
        :rtype: int
        """
        return self._booking_notification

    @booking_notification.setter
    def booking_notification(self, booking_notification):
        """Sets the booking_notification of this ResourceOptionsInputModel.


        :param booking_notification: The booking_notification of this ResourceOptionsInputModel.
        :type booking_notification: int
        """

        self._booking_notification = booking_notification

    @property
    def calendar_availability(self):
        """Gets the calendar_availability of this ResourceOptionsInputModel.

        0 = OnSched Availability, 1 = Google Calendar, 2 = Outlook Calendar

        :return: The calendar_availability of this ResourceOptionsInputModel.
        :rtype: int
        """
        return self._calendar_availability

    @calendar_availability.setter
    def calendar_availability(self, calendar_availability):
        """Sets the calendar_availability of this ResourceOptionsInputModel.

        0 = OnSched Availability, 1 = Google Calendar, 2 = Outlook Calendar

        :param calendar_availability: The calendar_availability of this ResourceOptionsInputModel.
        :type calendar_availability: int
        """

        self._calendar_availability = calendar_availability

    @property
    def display_color(self):
        """Gets the display_color of this ResourceOptionsInputModel.


        :return: The display_color of this ResourceOptionsInputModel.
        :rtype: str
        """
        return self._display_color

    @display_color.setter
    def display_color(self, display_color):
        """Sets the display_color of this ResourceOptionsInputModel.


        :param display_color: The display_color of this ResourceOptionsInputModel.
        :type display_color: str
        """

        self._display_color = display_color

    @property
    def effective_date(self):
        """Gets the effective_date of this ResourceOptionsInputModel.


        :return: The effective_date of this ResourceOptionsInputModel.
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this ResourceOptionsInputModel.


        :param effective_date: The effective_date of this ResourceOptionsInputModel.
        :type effective_date: datetime
        """

        self._effective_date = effective_date

    @property
    def gender(self):
        """Gets the gender of this ResourceOptionsInputModel.


        :return: The gender of this ResourceOptionsInputModel.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this ResourceOptionsInputModel.


        :param gender: The gender of this ResourceOptionsInputModel.
        :type gender: str
        """

        self._gender = gender

    @property
    def google_calendar_id(self):
        """Gets the google_calendar_id of this ResourceOptionsInputModel.


        :return: The google_calendar_id of this ResourceOptionsInputModel.
        :rtype: str
        """
        return self._google_calendar_id

    @google_calendar_id.setter
    def google_calendar_id(self, google_calendar_id):
        """Sets the google_calendar_id of this ResourceOptionsInputModel.


        :param google_calendar_id: The google_calendar_id of this ResourceOptionsInputModel.
        :type google_calendar_id: str
        """

        self._google_calendar_id = google_calendar_id

    @property
    def hourly(self):
        """Gets the hourly of this ResourceOptionsInputModel.


        :return: The hourly of this ResourceOptionsInputModel.
        :rtype: float
        """
        return self._hourly

    @hourly.setter
    def hourly(self, hourly):
        """Sets the hourly of this ResourceOptionsInputModel.


        :param hourly: The hourly of this ResourceOptionsInputModel.
        :type hourly: float
        """

        self._hourly = hourly

    @property
    def ignore_business_hours(self):
        """Gets the ignore_business_hours of this ResourceOptionsInputModel.


        :return: The ignore_business_hours of this ResourceOptionsInputModel.
        :rtype: bool
        """
        return self._ignore_business_hours

    @ignore_business_hours.setter
    def ignore_business_hours(self, ignore_business_hours):
        """Sets the ignore_business_hours of this ResourceOptionsInputModel.


        :param ignore_business_hours: The ignore_business_hours of this ResourceOptionsInputModel.
        :type ignore_business_hours: bool
        """

        self._ignore_business_hours = ignore_business_hours

    @property
    def notification_type(self):
        """Gets the notification_type of this ResourceOptionsInputModel.

        0 = None, 1=Online Bookings 2=All Bookings.

        :return: The notification_type of this ResourceOptionsInputModel.
        :rtype: int
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this ResourceOptionsInputModel.

        0 = None, 1=Online Bookings 2=All Bookings.

        :param notification_type: The notification_type of this ResourceOptionsInputModel.
        :type notification_type: int
        """

        self._notification_type = notification_type

    @property
    def outlook_calendar_id(self):
        """Gets the outlook_calendar_id of this ResourceOptionsInputModel.


        :return: The outlook_calendar_id of this ResourceOptionsInputModel.
        :rtype: str
        """
        return self._outlook_calendar_id

    @outlook_calendar_id.setter
    def outlook_calendar_id(self, outlook_calendar_id):
        """Sets the outlook_calendar_id of this ResourceOptionsInputModel.


        :param outlook_calendar_id: The outlook_calendar_id of this ResourceOptionsInputModel.
        :type outlook_calendar_id: str
        """

        self._outlook_calendar_id = outlook_calendar_id

    @property
    def sort_key(self):
        """Gets the sort_key of this ResourceOptionsInputModel.


        :return: The sort_key of this ResourceOptionsInputModel.
        :rtype: int
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ResourceOptionsInputModel.


        :param sort_key: The sort_key of this ResourceOptionsInputModel.
        :type sort_key: int
        """

        self._sort_key = sort_key
