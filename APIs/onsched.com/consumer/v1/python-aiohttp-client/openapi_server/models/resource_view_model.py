# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.address_view_model import AddressViewModel
from openapi_server.models.contact_view_model import ContactViewModel
from openapi_server.models.custom_field_input_model import CustomFieldInputModel
from openapi_server.models.resource_hours_view_model import ResourceHoursViewModel
from openapi_server.models.resource_service_view_model import ResourceServiceViewModel
from openapi_server import util


class ResourceViewModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address: AddressViewModel=None, availability: ResourceHoursViewModel=None, bio_link: str=None, booking_notification: int=None, calendar_availability: int=None, contact: ContactViewModel=None, custom_fields: CustomFieldInputModel=None, deleted_status: bool=None, deleted_time: datetime=None, description: str=None, effective_date: datetime=None, email: str=None, gender: str=None, google_calendar_id: str=None, group_id: str=None, hourly: float=None, id: str=None, ignore_business_hours: bool=None, image_url: str=None, location_id: str=None, name: str=None, notification_type: int=None, object: str=None, outlook_calendar_id: str=None, recurring_availability: bool=None, services: List[ResourceServiceViewModel]=None, skype_name: str=None, sort_key: int=None, timezone_iana: str=None, timezone_id: str=None, timezone_offset: int=None):
        """ResourceViewModel - a model defined in OpenAPI

        :param address: The address of this ResourceViewModel.
        :param availability: The availability of this ResourceViewModel.
        :param bio_link: The bio_link of this ResourceViewModel.
        :param booking_notification: The booking_notification of this ResourceViewModel.
        :param calendar_availability: The calendar_availability of this ResourceViewModel.
        :param contact: The contact of this ResourceViewModel.
        :param custom_fields: The custom_fields of this ResourceViewModel.
        :param deleted_status: The deleted_status of this ResourceViewModel.
        :param deleted_time: The deleted_time of this ResourceViewModel.
        :param description: The description of this ResourceViewModel.
        :param effective_date: The effective_date of this ResourceViewModel.
        :param email: The email of this ResourceViewModel.
        :param gender: The gender of this ResourceViewModel.
        :param google_calendar_id: The google_calendar_id of this ResourceViewModel.
        :param group_id: The group_id of this ResourceViewModel.
        :param hourly: The hourly of this ResourceViewModel.
        :param id: The id of this ResourceViewModel.
        :param ignore_business_hours: The ignore_business_hours of this ResourceViewModel.
        :param image_url: The image_url of this ResourceViewModel.
        :param location_id: The location_id of this ResourceViewModel.
        :param name: The name of this ResourceViewModel.
        :param notification_type: The notification_type of this ResourceViewModel.
        :param object: The object of this ResourceViewModel.
        :param outlook_calendar_id: The outlook_calendar_id of this ResourceViewModel.
        :param recurring_availability: The recurring_availability of this ResourceViewModel.
        :param services: The services of this ResourceViewModel.
        :param skype_name: The skype_name of this ResourceViewModel.
        :param sort_key: The sort_key of this ResourceViewModel.
        :param timezone_iana: The timezone_iana of this ResourceViewModel.
        :param timezone_id: The timezone_id of this ResourceViewModel.
        :param timezone_offset: The timezone_offset of this ResourceViewModel.
        """
        self.openapi_types = {
            'address': AddressViewModel,
            'availability': ResourceHoursViewModel,
            'bio_link': str,
            'booking_notification': int,
            'calendar_availability': int,
            'contact': ContactViewModel,
            'custom_fields': CustomFieldInputModel,
            'deleted_status': bool,
            'deleted_time': datetime,
            'description': str,
            'effective_date': datetime,
            'email': str,
            'gender': str,
            'google_calendar_id': str,
            'group_id': str,
            'hourly': float,
            'id': str,
            'ignore_business_hours': bool,
            'image_url': str,
            'location_id': str,
            'name': str,
            'notification_type': int,
            'object': str,
            'outlook_calendar_id': str,
            'recurring_availability': bool,
            'services': List[ResourceServiceViewModel],
            'skype_name': str,
            'sort_key': int,
            'timezone_iana': str,
            'timezone_id': str,
            'timezone_offset': int
        }

        self.attribute_map = {
            'address': 'address',
            'availability': 'availability',
            'bio_link': 'bioLink',
            'booking_notification': 'bookingNotification',
            'calendar_availability': 'calendarAvailability',
            'contact': 'contact',
            'custom_fields': 'customFields',
            'deleted_status': 'deletedStatus',
            'deleted_time': 'deletedTime',
            'description': 'description',
            'effective_date': 'effectiveDate',
            'email': 'email',
            'gender': 'gender',
            'google_calendar_id': 'googleCalendarId',
            'group_id': 'groupId',
            'hourly': 'hourly',
            'id': 'id',
            'ignore_business_hours': 'ignoreBusinessHours',
            'image_url': 'imageUrl',
            'location_id': 'locationId',
            'name': 'name',
            'notification_type': 'notificationType',
            'object': 'object',
            'outlook_calendar_id': 'outlookCalendarId',
            'recurring_availability': 'recurringAvailability',
            'services': 'services',
            'skype_name': 'skypeName',
            'sort_key': 'sortKey',
            'timezone_iana': 'timezoneIana',
            'timezone_id': 'timezoneId',
            'timezone_offset': 'timezoneOffset'
        }

        self._address = address
        self._availability = availability
        self._bio_link = bio_link
        self._booking_notification = booking_notification
        self._calendar_availability = calendar_availability
        self._contact = contact
        self._custom_fields = custom_fields
        self._deleted_status = deleted_status
        self._deleted_time = deleted_time
        self._description = description
        self._effective_date = effective_date
        self._email = email
        self._gender = gender
        self._google_calendar_id = google_calendar_id
        self._group_id = group_id
        self._hourly = hourly
        self._id = id
        self._ignore_business_hours = ignore_business_hours
        self._image_url = image_url
        self._location_id = location_id
        self._name = name
        self._notification_type = notification_type
        self._object = object
        self._outlook_calendar_id = outlook_calendar_id
        self._recurring_availability = recurring_availability
        self._services = services
        self._skype_name = skype_name
        self._sort_key = sort_key
        self._timezone_iana = timezone_iana
        self._timezone_id = timezone_id
        self._timezone_offset = timezone_offset

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ResourceViewModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ResourceViewModel of this ResourceViewModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this ResourceViewModel.


        :return: The address of this ResourceViewModel.
        :rtype: AddressViewModel
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ResourceViewModel.


        :param address: The address of this ResourceViewModel.
        :type address: AddressViewModel
        """

        self._address = address

    @property
    def availability(self):
        """Gets the availability of this ResourceViewModel.


        :return: The availability of this ResourceViewModel.
        :rtype: ResourceHoursViewModel
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this ResourceViewModel.


        :param availability: The availability of this ResourceViewModel.
        :type availability: ResourceHoursViewModel
        """

        self._availability = availability

    @property
    def bio_link(self):
        """Gets the bio_link of this ResourceViewModel.


        :return: The bio_link of this ResourceViewModel.
        :rtype: str
        """
        return self._bio_link

    @bio_link.setter
    def bio_link(self, bio_link):
        """Sets the bio_link of this ResourceViewModel.


        :param bio_link: The bio_link of this ResourceViewModel.
        :type bio_link: str
        """

        self._bio_link = bio_link

    @property
    def booking_notification(self):
        """Gets the booking_notification of this ResourceViewModel.


        :return: The booking_notification of this ResourceViewModel.
        :rtype: int
        """
        return self._booking_notification

    @booking_notification.setter
    def booking_notification(self, booking_notification):
        """Sets the booking_notification of this ResourceViewModel.


        :param booking_notification: The booking_notification of this ResourceViewModel.
        :type booking_notification: int
        """

        self._booking_notification = booking_notification

    @property
    def calendar_availability(self):
        """Gets the calendar_availability of this ResourceViewModel.


        :return: The calendar_availability of this ResourceViewModel.
        :rtype: int
        """
        return self._calendar_availability

    @calendar_availability.setter
    def calendar_availability(self, calendar_availability):
        """Sets the calendar_availability of this ResourceViewModel.


        :param calendar_availability: The calendar_availability of this ResourceViewModel.
        :type calendar_availability: int
        """

        self._calendar_availability = calendar_availability

    @property
    def contact(self):
        """Gets the contact of this ResourceViewModel.


        :return: The contact of this ResourceViewModel.
        :rtype: ContactViewModel
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this ResourceViewModel.


        :param contact: The contact of this ResourceViewModel.
        :type contact: ContactViewModel
        """

        self._contact = contact

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ResourceViewModel.


        :return: The custom_fields of this ResourceViewModel.
        :rtype: CustomFieldInputModel
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ResourceViewModel.


        :param custom_fields: The custom_fields of this ResourceViewModel.
        :type custom_fields: CustomFieldInputModel
        """

        self._custom_fields = custom_fields

    @property
    def deleted_status(self):
        """Gets the deleted_status of this ResourceViewModel.


        :return: The deleted_status of this ResourceViewModel.
        :rtype: bool
        """
        return self._deleted_status

    @deleted_status.setter
    def deleted_status(self, deleted_status):
        """Sets the deleted_status of this ResourceViewModel.


        :param deleted_status: The deleted_status of this ResourceViewModel.
        :type deleted_status: bool
        """

        self._deleted_status = deleted_status

    @property
    def deleted_time(self):
        """Gets the deleted_time of this ResourceViewModel.


        :return: The deleted_time of this ResourceViewModel.
        :rtype: datetime
        """
        return self._deleted_time

    @deleted_time.setter
    def deleted_time(self, deleted_time):
        """Sets the deleted_time of this ResourceViewModel.


        :param deleted_time: The deleted_time of this ResourceViewModel.
        :type deleted_time: datetime
        """

        self._deleted_time = deleted_time

    @property
    def description(self):
        """Gets the description of this ResourceViewModel.


        :return: The description of this ResourceViewModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResourceViewModel.


        :param description: The description of this ResourceViewModel.
        :type description: str
        """

        self._description = description

    @property
    def effective_date(self):
        """Gets the effective_date of this ResourceViewModel.


        :return: The effective_date of this ResourceViewModel.
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this ResourceViewModel.


        :param effective_date: The effective_date of this ResourceViewModel.
        :type effective_date: datetime
        """

        self._effective_date = effective_date

    @property
    def email(self):
        """Gets the email of this ResourceViewModel.


        :return: The email of this ResourceViewModel.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ResourceViewModel.


        :param email: The email of this ResourceViewModel.
        :type email: str
        """

        self._email = email

    @property
    def gender(self):
        """Gets the gender of this ResourceViewModel.


        :return: The gender of this ResourceViewModel.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this ResourceViewModel.


        :param gender: The gender of this ResourceViewModel.
        :type gender: str
        """

        self._gender = gender

    @property
    def google_calendar_id(self):
        """Gets the google_calendar_id of this ResourceViewModel.


        :return: The google_calendar_id of this ResourceViewModel.
        :rtype: str
        """
        return self._google_calendar_id

    @google_calendar_id.setter
    def google_calendar_id(self, google_calendar_id):
        """Sets the google_calendar_id of this ResourceViewModel.


        :param google_calendar_id: The google_calendar_id of this ResourceViewModel.
        :type google_calendar_id: str
        """

        self._google_calendar_id = google_calendar_id

    @property
    def group_id(self):
        """Gets the group_id of this ResourceViewModel.


        :return: The group_id of this ResourceViewModel.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ResourceViewModel.


        :param group_id: The group_id of this ResourceViewModel.
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def hourly(self):
        """Gets the hourly of this ResourceViewModel.


        :return: The hourly of this ResourceViewModel.
        :rtype: float
        """
        return self._hourly

    @hourly.setter
    def hourly(self, hourly):
        """Sets the hourly of this ResourceViewModel.


        :param hourly: The hourly of this ResourceViewModel.
        :type hourly: float
        """

        self._hourly = hourly

    @property
    def id(self):
        """Gets the id of this ResourceViewModel.


        :return: The id of this ResourceViewModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceViewModel.


        :param id: The id of this ResourceViewModel.
        :type id: str
        """

        self._id = id

    @property
    def ignore_business_hours(self):
        """Gets the ignore_business_hours of this ResourceViewModel.


        :return: The ignore_business_hours of this ResourceViewModel.
        :rtype: bool
        """
        return self._ignore_business_hours

    @ignore_business_hours.setter
    def ignore_business_hours(self, ignore_business_hours):
        """Sets the ignore_business_hours of this ResourceViewModel.


        :param ignore_business_hours: The ignore_business_hours of this ResourceViewModel.
        :type ignore_business_hours: bool
        """

        self._ignore_business_hours = ignore_business_hours

    @property
    def image_url(self):
        """Gets the image_url of this ResourceViewModel.


        :return: The image_url of this ResourceViewModel.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ResourceViewModel.


        :param image_url: The image_url of this ResourceViewModel.
        :type image_url: str
        """

        self._image_url = image_url

    @property
    def location_id(self):
        """Gets the location_id of this ResourceViewModel.


        :return: The location_id of this ResourceViewModel.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this ResourceViewModel.


        :param location_id: The location_id of this ResourceViewModel.
        :type location_id: str
        """

        self._location_id = location_id

    @property
    def name(self):
        """Gets the name of this ResourceViewModel.


        :return: The name of this ResourceViewModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceViewModel.


        :param name: The name of this ResourceViewModel.
        :type name: str
        """

        self._name = name

    @property
    def notification_type(self):
        """Gets the notification_type of this ResourceViewModel.


        :return: The notification_type of this ResourceViewModel.
        :rtype: int
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this ResourceViewModel.


        :param notification_type: The notification_type of this ResourceViewModel.
        :type notification_type: int
        """

        self._notification_type = notification_type

    @property
    def object(self):
        """Gets the object of this ResourceViewModel.


        :return: The object of this ResourceViewModel.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this ResourceViewModel.


        :param object: The object of this ResourceViewModel.
        :type object: str
        """

        self._object = object

    @property
    def outlook_calendar_id(self):
        """Gets the outlook_calendar_id of this ResourceViewModel.


        :return: The outlook_calendar_id of this ResourceViewModel.
        :rtype: str
        """
        return self._outlook_calendar_id

    @outlook_calendar_id.setter
    def outlook_calendar_id(self, outlook_calendar_id):
        """Sets the outlook_calendar_id of this ResourceViewModel.


        :param outlook_calendar_id: The outlook_calendar_id of this ResourceViewModel.
        :type outlook_calendar_id: str
        """

        self._outlook_calendar_id = outlook_calendar_id

    @property
    def recurring_availability(self):
        """Gets the recurring_availability of this ResourceViewModel.


        :return: The recurring_availability of this ResourceViewModel.
        :rtype: bool
        """
        return self._recurring_availability

    @recurring_availability.setter
    def recurring_availability(self, recurring_availability):
        """Sets the recurring_availability of this ResourceViewModel.


        :param recurring_availability: The recurring_availability of this ResourceViewModel.
        :type recurring_availability: bool
        """

        self._recurring_availability = recurring_availability

    @property
    def services(self):
        """Gets the services of this ResourceViewModel.


        :return: The services of this ResourceViewModel.
        :rtype: List[ResourceServiceViewModel]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this ResourceViewModel.


        :param services: The services of this ResourceViewModel.
        :type services: List[ResourceServiceViewModel]
        """

        self._services = services

    @property
    def skype_name(self):
        """Gets the skype_name of this ResourceViewModel.


        :return: The skype_name of this ResourceViewModel.
        :rtype: str
        """
        return self._skype_name

    @skype_name.setter
    def skype_name(self, skype_name):
        """Sets the skype_name of this ResourceViewModel.


        :param skype_name: The skype_name of this ResourceViewModel.
        :type skype_name: str
        """

        self._skype_name = skype_name

    @property
    def sort_key(self):
        """Gets the sort_key of this ResourceViewModel.


        :return: The sort_key of this ResourceViewModel.
        :rtype: int
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ResourceViewModel.


        :param sort_key: The sort_key of this ResourceViewModel.
        :type sort_key: int
        """

        self._sort_key = sort_key

    @property
    def timezone_iana(self):
        """Gets the timezone_iana of this ResourceViewModel.


        :return: The timezone_iana of this ResourceViewModel.
        :rtype: str
        """
        return self._timezone_iana

    @timezone_iana.setter
    def timezone_iana(self, timezone_iana):
        """Sets the timezone_iana of this ResourceViewModel.


        :param timezone_iana: The timezone_iana of this ResourceViewModel.
        :type timezone_iana: str
        """

        self._timezone_iana = timezone_iana

    @property
    def timezone_id(self):
        """Gets the timezone_id of this ResourceViewModel.


        :return: The timezone_id of this ResourceViewModel.
        :rtype: str
        """
        return self._timezone_id

    @timezone_id.setter
    def timezone_id(self, timezone_id):
        """Sets the timezone_id of this ResourceViewModel.


        :param timezone_id: The timezone_id of this ResourceViewModel.
        :type timezone_id: str
        """

        self._timezone_id = timezone_id

    @property
    def timezone_offset(self):
        """Gets the timezone_offset of this ResourceViewModel.


        :return: The timezone_offset of this ResourceViewModel.
        :rtype: int
        """
        return self._timezone_offset

    @timezone_offset.setter
    def timezone_offset(self, timezone_offset):
        """Sets the timezone_offset of this ResourceViewModel.


        :param timezone_offset: The timezone_offset of this ResourceViewModel.
        :type timezone_offset: int
        """

        self._timezone_offset = timezone_offset
