# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.booking_field_item import BookingFieldItem
from openapi_server.models.custom_field_input_model import CustomFieldInputModel
from openapi_server import util


class AppointmentInitialModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, appointment_booking_fields: List[BookingFieldItem]=None, booked_by: str=None, booking_window_id: str=None, calendar_id: str=None, custom_fields: CustomFieldInputModel=None, customer_booking_fields: List[BookingFieldItem]=None, customer_id: str=None, customer_message: str=None, email: str=None, end_date_time: datetime=None, group_size: int=None, location: str=None, location_id: str=None, name: str=None, notes: str=None, phone: str=None, phone_type: str=None, resource_group_id: str=None, resource_id: str=None, resource_ids: str=None, service_allocation_id: str=None, service_id: str=None, start_date_time: datetime=None, timezone_name: str=None, travel_appointment_id: str=None, travel_time_mins: int=None):
        """AppointmentInitialModel - a model defined in OpenAPI

        :param appointment_booking_fields: The appointment_booking_fields of this AppointmentInitialModel.
        :param booked_by: The booked_by of this AppointmentInitialModel.
        :param booking_window_id: The booking_window_id of this AppointmentInitialModel.
        :param calendar_id: The calendar_id of this AppointmentInitialModel.
        :param custom_fields: The custom_fields of this AppointmentInitialModel.
        :param customer_booking_fields: The customer_booking_fields of this AppointmentInitialModel.
        :param customer_id: The customer_id of this AppointmentInitialModel.
        :param customer_message: The customer_message of this AppointmentInitialModel.
        :param email: The email of this AppointmentInitialModel.
        :param end_date_time: The end_date_time of this AppointmentInitialModel.
        :param group_size: The group_size of this AppointmentInitialModel.
        :param location: The location of this AppointmentInitialModel.
        :param location_id: The location_id of this AppointmentInitialModel.
        :param name: The name of this AppointmentInitialModel.
        :param notes: The notes of this AppointmentInitialModel.
        :param phone: The phone of this AppointmentInitialModel.
        :param phone_type: The phone_type of this AppointmentInitialModel.
        :param resource_group_id: The resource_group_id of this AppointmentInitialModel.
        :param resource_id: The resource_id of this AppointmentInitialModel.
        :param resource_ids: The resource_ids of this AppointmentInitialModel.
        :param service_allocation_id: The service_allocation_id of this AppointmentInitialModel.
        :param service_id: The service_id of this AppointmentInitialModel.
        :param start_date_time: The start_date_time of this AppointmentInitialModel.
        :param timezone_name: The timezone_name of this AppointmentInitialModel.
        :param travel_appointment_id: The travel_appointment_id of this AppointmentInitialModel.
        :param travel_time_mins: The travel_time_mins of this AppointmentInitialModel.
        """
        self.openapi_types = {
            'appointment_booking_fields': List[BookingFieldItem],
            'booked_by': str,
            'booking_window_id': str,
            'calendar_id': str,
            'custom_fields': CustomFieldInputModel,
            'customer_booking_fields': List[BookingFieldItem],
            'customer_id': str,
            'customer_message': str,
            'email': str,
            'end_date_time': datetime,
            'group_size': int,
            'location': str,
            'location_id': str,
            'name': str,
            'notes': str,
            'phone': str,
            'phone_type': str,
            'resource_group_id': str,
            'resource_id': str,
            'resource_ids': str,
            'service_allocation_id': str,
            'service_id': str,
            'start_date_time': datetime,
            'timezone_name': str,
            'travel_appointment_id': str,
            'travel_time_mins': int
        }

        self.attribute_map = {
            'appointment_booking_fields': 'appointmentBookingFields',
            'booked_by': 'bookedBy',
            'booking_window_id': 'bookingWindowId',
            'calendar_id': 'calendarId',
            'custom_fields': 'customFields',
            'customer_booking_fields': 'customerBookingFields',
            'customer_id': 'customerId',
            'customer_message': 'customerMessage',
            'email': 'email',
            'end_date_time': 'endDateTime',
            'group_size': 'groupSize',
            'location': 'location',
            'location_id': 'locationId',
            'name': 'name',
            'notes': 'notes',
            'phone': 'phone',
            'phone_type': 'phoneType',
            'resource_group_id': 'resourceGroupId',
            'resource_id': 'resourceId',
            'resource_ids': 'resourceIds',
            'service_allocation_id': 'serviceAllocationId',
            'service_id': 'serviceId',
            'start_date_time': 'startDateTime',
            'timezone_name': 'timezoneName',
            'travel_appointment_id': 'travelAppointmentId',
            'travel_time_mins': 'travelTimeMins'
        }

        self._appointment_booking_fields = appointment_booking_fields
        self._booked_by = booked_by
        self._booking_window_id = booking_window_id
        self._calendar_id = calendar_id
        self._custom_fields = custom_fields
        self._customer_booking_fields = customer_booking_fields
        self._customer_id = customer_id
        self._customer_message = customer_message
        self._email = email
        self._end_date_time = end_date_time
        self._group_size = group_size
        self._location = location
        self._location_id = location_id
        self._name = name
        self._notes = notes
        self._phone = phone
        self._phone_type = phone_type
        self._resource_group_id = resource_group_id
        self._resource_id = resource_id
        self._resource_ids = resource_ids
        self._service_allocation_id = service_allocation_id
        self._service_id = service_id
        self._start_date_time = start_date_time
        self._timezone_name = timezone_name
        self._travel_appointment_id = travel_appointment_id
        self._travel_time_mins = travel_time_mins

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AppointmentInitialModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AppointmentInitialModel of this AppointmentInitialModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def appointment_booking_fields(self):
        """Gets the appointment_booking_fields of this AppointmentInitialModel.


        :return: The appointment_booking_fields of this AppointmentInitialModel.
        :rtype: List[BookingFieldItem]
        """
        return self._appointment_booking_fields

    @appointment_booking_fields.setter
    def appointment_booking_fields(self, appointment_booking_fields):
        """Sets the appointment_booking_fields of this AppointmentInitialModel.


        :param appointment_booking_fields: The appointment_booking_fields of this AppointmentInitialModel.
        :type appointment_booking_fields: List[BookingFieldItem]
        """

        self._appointment_booking_fields = appointment_booking_fields

    @property
    def booked_by(self):
        """Gets the booked_by of this AppointmentInitialModel.


        :return: The booked_by of this AppointmentInitialModel.
        :rtype: str
        """
        return self._booked_by

    @booked_by.setter
    def booked_by(self, booked_by):
        """Sets the booked_by of this AppointmentInitialModel.


        :param booked_by: The booked_by of this AppointmentInitialModel.
        :type booked_by: str
        """

        self._booked_by = booked_by

    @property
    def booking_window_id(self):
        """Gets the booking_window_id of this AppointmentInitialModel.


        :return: The booking_window_id of this AppointmentInitialModel.
        :rtype: str
        """
        return self._booking_window_id

    @booking_window_id.setter
    def booking_window_id(self, booking_window_id):
        """Sets the booking_window_id of this AppointmentInitialModel.


        :param booking_window_id: The booking_window_id of this AppointmentInitialModel.
        :type booking_window_id: str
        """

        self._booking_window_id = booking_window_id

    @property
    def calendar_id(self):
        """Gets the calendar_id of this AppointmentInitialModel.


        :return: The calendar_id of this AppointmentInitialModel.
        :rtype: str
        """
        return self._calendar_id

    @calendar_id.setter
    def calendar_id(self, calendar_id):
        """Sets the calendar_id of this AppointmentInitialModel.


        :param calendar_id: The calendar_id of this AppointmentInitialModel.
        :type calendar_id: str
        """

        self._calendar_id = calendar_id

    @property
    def custom_fields(self):
        """Gets the custom_fields of this AppointmentInitialModel.


        :return: The custom_fields of this AppointmentInitialModel.
        :rtype: CustomFieldInputModel
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this AppointmentInitialModel.


        :param custom_fields: The custom_fields of this AppointmentInitialModel.
        :type custom_fields: CustomFieldInputModel
        """

        self._custom_fields = custom_fields

    @property
    def customer_booking_fields(self):
        """Gets the customer_booking_fields of this AppointmentInitialModel.


        :return: The customer_booking_fields of this AppointmentInitialModel.
        :rtype: List[BookingFieldItem]
        """
        return self._customer_booking_fields

    @customer_booking_fields.setter
    def customer_booking_fields(self, customer_booking_fields):
        """Sets the customer_booking_fields of this AppointmentInitialModel.


        :param customer_booking_fields: The customer_booking_fields of this AppointmentInitialModel.
        :type customer_booking_fields: List[BookingFieldItem]
        """

        self._customer_booking_fields = customer_booking_fields

    @property
    def customer_id(self):
        """Gets the customer_id of this AppointmentInitialModel.


        :return: The customer_id of this AppointmentInitialModel.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AppointmentInitialModel.


        :param customer_id: The customer_id of this AppointmentInitialModel.
        :type customer_id: str
        """

        self._customer_id = customer_id

    @property
    def customer_message(self):
        """Gets the customer_message of this AppointmentInitialModel.


        :return: The customer_message of this AppointmentInitialModel.
        :rtype: str
        """
        return self._customer_message

    @customer_message.setter
    def customer_message(self, customer_message):
        """Sets the customer_message of this AppointmentInitialModel.


        :param customer_message: The customer_message of this AppointmentInitialModel.
        :type customer_message: str
        """

        self._customer_message = customer_message

    @property
    def email(self):
        """Gets the email of this AppointmentInitialModel.


        :return: The email of this AppointmentInitialModel.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AppointmentInitialModel.


        :param email: The email of this AppointmentInitialModel.
        :type email: str
        """

        self._email = email

    @property
    def end_date_time(self):
        """Gets the end_date_time of this AppointmentInitialModel.


        :return: The end_date_time of this AppointmentInitialModel.
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this AppointmentInitialModel.


        :param end_date_time: The end_date_time of this AppointmentInitialModel.
        :type end_date_time: datetime
        """

        self._end_date_time = end_date_time

    @property
    def group_size(self):
        """Gets the group_size of this AppointmentInitialModel.


        :return: The group_size of this AppointmentInitialModel.
        :rtype: int
        """
        return self._group_size

    @group_size.setter
    def group_size(self, group_size):
        """Sets the group_size of this AppointmentInitialModel.


        :param group_size: The group_size of this AppointmentInitialModel.
        :type group_size: int
        """

        self._group_size = group_size

    @property
    def location(self):
        """Gets the location of this AppointmentInitialModel.


        :return: The location of this AppointmentInitialModel.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this AppointmentInitialModel.


        :param location: The location of this AppointmentInitialModel.
        :type location: str
        """

        self._location = location

    @property
    def location_id(self):
        """Gets the location_id of this AppointmentInitialModel.


        :return: The location_id of this AppointmentInitialModel.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this AppointmentInitialModel.


        :param location_id: The location_id of this AppointmentInitialModel.
        :type location_id: str
        """

        self._location_id = location_id

    @property
    def name(self):
        """Gets the name of this AppointmentInitialModel.


        :return: The name of this AppointmentInitialModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppointmentInitialModel.


        :param name: The name of this AppointmentInitialModel.
        :type name: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this AppointmentInitialModel.


        :return: The notes of this AppointmentInitialModel.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this AppointmentInitialModel.


        :param notes: The notes of this AppointmentInitialModel.
        :type notes: str
        """

        self._notes = notes

    @property
    def phone(self):
        """Gets the phone of this AppointmentInitialModel.


        :return: The phone of this AppointmentInitialModel.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this AppointmentInitialModel.


        :param phone: The phone of this AppointmentInitialModel.
        :type phone: str
        """

        self._phone = phone

    @property
    def phone_type(self):
        """Gets the phone_type of this AppointmentInitialModel.


        :return: The phone_type of this AppointmentInitialModel.
        :rtype: str
        """
        return self._phone_type

    @phone_type.setter
    def phone_type(self, phone_type):
        """Sets the phone_type of this AppointmentInitialModel.


        :param phone_type: The phone_type of this AppointmentInitialModel.
        :type phone_type: str
        """

        self._phone_type = phone_type

    @property
    def resource_group_id(self):
        """Gets the resource_group_id of this AppointmentInitialModel.


        :return: The resource_group_id of this AppointmentInitialModel.
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        """Sets the resource_group_id of this AppointmentInitialModel.


        :param resource_group_id: The resource_group_id of this AppointmentInitialModel.
        :type resource_group_id: str
        """

        self._resource_group_id = resource_group_id

    @property
    def resource_id(self):
        """Gets the resource_id of this AppointmentInitialModel.


        :return: The resource_id of this AppointmentInitialModel.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this AppointmentInitialModel.


        :param resource_id: The resource_id of this AppointmentInitialModel.
        :type resource_id: str
        """

        self._resource_id = resource_id

    @property
    def resource_ids(self):
        """Gets the resource_ids of this AppointmentInitialModel.


        :return: The resource_ids of this AppointmentInitialModel.
        :rtype: str
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this AppointmentInitialModel.


        :param resource_ids: The resource_ids of this AppointmentInitialModel.
        :type resource_ids: str
        """

        self._resource_ids = resource_ids

    @property
    def service_allocation_id(self):
        """Gets the service_allocation_id of this AppointmentInitialModel.


        :return: The service_allocation_id of this AppointmentInitialModel.
        :rtype: str
        """
        return self._service_allocation_id

    @service_allocation_id.setter
    def service_allocation_id(self, service_allocation_id):
        """Sets the service_allocation_id of this AppointmentInitialModel.


        :param service_allocation_id: The service_allocation_id of this AppointmentInitialModel.
        :type service_allocation_id: str
        """

        self._service_allocation_id = service_allocation_id

    @property
    def service_id(self):
        """Gets the service_id of this AppointmentInitialModel.


        :return: The service_id of this AppointmentInitialModel.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this AppointmentInitialModel.


        :param service_id: The service_id of this AppointmentInitialModel.
        :type service_id: str
        """

        self._service_id = service_id

    @property
    def start_date_time(self):
        """Gets the start_date_time of this AppointmentInitialModel.


        :return: The start_date_time of this AppointmentInitialModel.
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this AppointmentInitialModel.


        :param start_date_time: The start_date_time of this AppointmentInitialModel.
        :type start_date_time: datetime
        """

        self._start_date_time = start_date_time

    @property
    def timezone_name(self):
        """Gets the timezone_name of this AppointmentInitialModel.


        :return: The timezone_name of this AppointmentInitialModel.
        :rtype: str
        """
        return self._timezone_name

    @timezone_name.setter
    def timezone_name(self, timezone_name):
        """Sets the timezone_name of this AppointmentInitialModel.


        :param timezone_name: The timezone_name of this AppointmentInitialModel.
        :type timezone_name: str
        """

        self._timezone_name = timezone_name

    @property
    def travel_appointment_id(self):
        """Gets the travel_appointment_id of this AppointmentInitialModel.


        :return: The travel_appointment_id of this AppointmentInitialModel.
        :rtype: str
        """
        return self._travel_appointment_id

    @travel_appointment_id.setter
    def travel_appointment_id(self, travel_appointment_id):
        """Sets the travel_appointment_id of this AppointmentInitialModel.


        :param travel_appointment_id: The travel_appointment_id of this AppointmentInitialModel.
        :type travel_appointment_id: str
        """

        self._travel_appointment_id = travel_appointment_id

    @property
    def travel_time_mins(self):
        """Gets the travel_time_mins of this AppointmentInitialModel.


        :return: The travel_time_mins of this AppointmentInitialModel.
        :rtype: int
        """
        return self._travel_time_mins

    @travel_time_mins.setter
    def travel_time_mins(self, travel_time_mins):
        """Sets the travel_time_mins of this AppointmentInitialModel.


        :param travel_time_mins: The travel_time_mins of this AppointmentInitialModel.
        :type travel_time_mins: int
        """

        self._travel_time_mins = travel_time_mins
