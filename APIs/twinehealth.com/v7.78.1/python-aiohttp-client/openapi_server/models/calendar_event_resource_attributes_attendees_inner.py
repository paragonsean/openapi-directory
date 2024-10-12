# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CalendarEventResourceAttributesAttendeesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, response_status: str=None, user: str=None):
        """CalendarEventResourceAttributesAttendeesInner - a model defined in OpenAPI

        :param response_status: The response_status of this CalendarEventResourceAttributesAttendeesInner.
        :param user: The user of this CalendarEventResourceAttributesAttendeesInner.
        """
        self.openapi_types = {
            'response_status': str,
            'user': str
        }

        self.attribute_map = {
            'response_status': 'response_status',
            'user': 'user'
        }

        self._response_status = response_status
        self._user = user

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CalendarEventResourceAttributesAttendeesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CalendarEventResource_attributes_attendees_inner of this CalendarEventResourceAttributesAttendeesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def response_status(self):
        """Gets the response_status of this CalendarEventResourceAttributesAttendeesInner.

        Status of responses from attendees

        :return: The response_status of this CalendarEventResourceAttributesAttendeesInner.
        :rtype: str
        """
        return self._response_status

    @response_status.setter
    def response_status(self, response_status):
        """Sets the response_status of this CalendarEventResourceAttributesAttendeesInner.

        Status of responses from attendees

        :param response_status: The response_status of this CalendarEventResourceAttributesAttendeesInner.
        :type response_status: str
        """
        allowed_values = ["needsAction", "declined", "tentative", "accepted"]  # noqa: E501
        if response_status not in allowed_values:
            raise ValueError(
                "Invalid value for `response_status` ({0}), must be one of {1}"
                .format(response_status, allowed_values)
            )

        self._response_status = response_status

    @property
    def user(self):
        """Gets the user of this CalendarEventResourceAttributesAttendeesInner.


        :return: The user of this CalendarEventResourceAttributesAttendeesInner.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this CalendarEventResourceAttributesAttendeesInner.


        :param user: The user of this CalendarEventResourceAttributesAttendeesInner.
        :type user: str
        """

        self._user = user
