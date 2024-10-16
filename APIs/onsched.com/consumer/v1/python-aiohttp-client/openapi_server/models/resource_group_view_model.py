# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ResourceGroupViewModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, booking_notification: int=None, deleted_status: bool=None, deleted_time: datetime=None, description: str=None, email: str=None, id: str=None, location_id: str=None, name: str=None, object: str=None):
        """ResourceGroupViewModel - a model defined in OpenAPI

        :param booking_notification: The booking_notification of this ResourceGroupViewModel.
        :param deleted_status: The deleted_status of this ResourceGroupViewModel.
        :param deleted_time: The deleted_time of this ResourceGroupViewModel.
        :param description: The description of this ResourceGroupViewModel.
        :param email: The email of this ResourceGroupViewModel.
        :param id: The id of this ResourceGroupViewModel.
        :param location_id: The location_id of this ResourceGroupViewModel.
        :param name: The name of this ResourceGroupViewModel.
        :param object: The object of this ResourceGroupViewModel.
        """
        self.openapi_types = {
            'booking_notification': int,
            'deleted_status': bool,
            'deleted_time': datetime,
            'description': str,
            'email': str,
            'id': str,
            'location_id': str,
            'name': str,
            'object': str
        }

        self.attribute_map = {
            'booking_notification': 'bookingNotification',
            'deleted_status': 'deletedStatus',
            'deleted_time': 'deletedTime',
            'description': 'description',
            'email': 'email',
            'id': 'id',
            'location_id': 'locationId',
            'name': 'name',
            'object': 'object'
        }

        self._booking_notification = booking_notification
        self._deleted_status = deleted_status
        self._deleted_time = deleted_time
        self._description = description
        self._email = email
        self._id = id
        self._location_id = location_id
        self._name = name
        self._object = object

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ResourceGroupViewModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ResourceGroupViewModel of this ResourceGroupViewModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def booking_notification(self):
        """Gets the booking_notification of this ResourceGroupViewModel.


        :return: The booking_notification of this ResourceGroupViewModel.
        :rtype: int
        """
        return self._booking_notification

    @booking_notification.setter
    def booking_notification(self, booking_notification):
        """Sets the booking_notification of this ResourceGroupViewModel.


        :param booking_notification: The booking_notification of this ResourceGroupViewModel.
        :type booking_notification: int
        """

        self._booking_notification = booking_notification

    @property
    def deleted_status(self):
        """Gets the deleted_status of this ResourceGroupViewModel.


        :return: The deleted_status of this ResourceGroupViewModel.
        :rtype: bool
        """
        return self._deleted_status

    @deleted_status.setter
    def deleted_status(self, deleted_status):
        """Sets the deleted_status of this ResourceGroupViewModel.


        :param deleted_status: The deleted_status of this ResourceGroupViewModel.
        :type deleted_status: bool
        """

        self._deleted_status = deleted_status

    @property
    def deleted_time(self):
        """Gets the deleted_time of this ResourceGroupViewModel.


        :return: The deleted_time of this ResourceGroupViewModel.
        :rtype: datetime
        """
        return self._deleted_time

    @deleted_time.setter
    def deleted_time(self, deleted_time):
        """Sets the deleted_time of this ResourceGroupViewModel.


        :param deleted_time: The deleted_time of this ResourceGroupViewModel.
        :type deleted_time: datetime
        """

        self._deleted_time = deleted_time

    @property
    def description(self):
        """Gets the description of this ResourceGroupViewModel.


        :return: The description of this ResourceGroupViewModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResourceGroupViewModel.


        :param description: The description of this ResourceGroupViewModel.
        :type description: str
        """

        self._description = description

    @property
    def email(self):
        """Gets the email of this ResourceGroupViewModel.


        :return: The email of this ResourceGroupViewModel.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ResourceGroupViewModel.


        :param email: The email of this ResourceGroupViewModel.
        :type email: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this ResourceGroupViewModel.


        :return: The id of this ResourceGroupViewModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceGroupViewModel.


        :param id: The id of this ResourceGroupViewModel.
        :type id: str
        """

        self._id = id

    @property
    def location_id(self):
        """Gets the location_id of this ResourceGroupViewModel.


        :return: The location_id of this ResourceGroupViewModel.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this ResourceGroupViewModel.


        :param location_id: The location_id of this ResourceGroupViewModel.
        :type location_id: str
        """

        self._location_id = location_id

    @property
    def name(self):
        """Gets the name of this ResourceGroupViewModel.


        :return: The name of this ResourceGroupViewModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceGroupViewModel.


        :param name: The name of this ResourceGroupViewModel.
        :type name: str
        """

        self._name = name

    @property
    def object(self):
        """Gets the object of this ResourceGroupViewModel.


        :return: The object of this ResourceGroupViewModel.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this ResourceGroupViewModel.


        :param object: The object of this ResourceGroupViewModel.
        :type object: str
        """

        self._object = object
