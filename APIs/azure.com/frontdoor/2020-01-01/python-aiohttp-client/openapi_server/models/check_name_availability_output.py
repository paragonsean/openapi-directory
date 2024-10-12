# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CheckNameAvailabilityOutput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message: str=None, name_availability: str=None, reason: str=None):
        """CheckNameAvailabilityOutput - a model defined in OpenAPI

        :param message: The message of this CheckNameAvailabilityOutput.
        :param name_availability: The name_availability of this CheckNameAvailabilityOutput.
        :param reason: The reason of this CheckNameAvailabilityOutput.
        """
        self.openapi_types = {
            'message': str,
            'name_availability': str,
            'reason': str
        }

        self.attribute_map = {
            'message': 'message',
            'name_availability': 'nameAvailability',
            'reason': 'reason'
        }

        self._message = message
        self._name_availability = name_availability
        self._reason = reason

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CheckNameAvailabilityOutput':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CheckNameAvailabilityOutput of this CheckNameAvailabilityOutput.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self):
        """Gets the message of this CheckNameAvailabilityOutput.

        The detailed error message describing why the name is not available.

        :return: The message of this CheckNameAvailabilityOutput.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CheckNameAvailabilityOutput.

        The detailed error message describing why the name is not available.

        :param message: The message of this CheckNameAvailabilityOutput.
        :type message: str
        """

        self._message = message

    @property
    def name_availability(self):
        """Gets the name_availability of this CheckNameAvailabilityOutput.

        Indicates whether the name is available.

        :return: The name_availability of this CheckNameAvailabilityOutput.
        :rtype: str
        """
        return self._name_availability

    @name_availability.setter
    def name_availability(self, name_availability):
        """Sets the name_availability of this CheckNameAvailabilityOutput.

        Indicates whether the name is available.

        :param name_availability: The name_availability of this CheckNameAvailabilityOutput.
        :type name_availability: str
        """
        allowed_values = ["Available", "Unavailable"]  # noqa: E501
        if name_availability not in allowed_values:
            raise ValueError(
                "Invalid value for `name_availability` ({0}), must be one of {1}"
                .format(name_availability, allowed_values)
            )

        self._name_availability = name_availability

    @property
    def reason(self):
        """Gets the reason of this CheckNameAvailabilityOutput.

        The reason why the name is not available.

        :return: The reason of this CheckNameAvailabilityOutput.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this CheckNameAvailabilityOutput.

        The reason why the name is not available.

        :param reason: The reason of this CheckNameAvailabilityOutput.
        :type reason: str
        """

        self._reason = reason
