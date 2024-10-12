# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.cancellation_type import CancellationType
from openapi_server.models.qualified_free_text import QualifiedFreeText
import re
from openapi_server import util


class HotelProductCancellationPolicy(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount: str=None, deadline: datetime=None, description: QualifiedFreeText=None, number_of_nights: int=None, percentage: str=None, type: CancellationType=None):
        """HotelProductCancellationPolicy - a model defined in OpenAPI

        :param amount: The amount of this HotelProductCancellationPolicy.
        :param deadline: The deadline of this HotelProductCancellationPolicy.
        :param description: The description of this HotelProductCancellationPolicy.
        :param number_of_nights: The number_of_nights of this HotelProductCancellationPolicy.
        :param percentage: The percentage of this HotelProductCancellationPolicy.
        :param type: The type of this HotelProductCancellationPolicy.
        """
        self.openapi_types = {
            'amount': str,
            'deadline': datetime,
            'description': QualifiedFreeText,
            'number_of_nights': int,
            'percentage': str,
            'type': CancellationType
        }

        self.attribute_map = {
            'amount': 'amount',
            'deadline': 'deadline',
            'description': 'description',
            'number_of_nights': 'numberOfNights',
            'percentage': 'percentage',
            'type': 'type'
        }

        self._amount = amount
        self._deadline = deadline
        self._description = description
        self._number_of_nights = number_of_nights
        self._percentage = percentage
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HotelProductCancellationPolicy':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HotelProduct_CancellationPolicy of this HotelProductCancellationPolicy.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self):
        """Gets the amount of this HotelProductCancellationPolicy.

        Amount of the cancellation fee.

        :return: The amount of this HotelProductCancellationPolicy.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this HotelProductCancellationPolicy.

        Amount of the cancellation fee.

        :param amount: The amount of this HotelProductCancellationPolicy.
        :type amount: str
        """
        if amount is not None and not re.search(r'^\\d+(\\.\\d+)?$', amount):
            raise ValueError("Invalid value for `amount`, must be a follow pattern or equal to `/^\\d+(\\.\\d+)?$/`")

        self._amount = amount

    @property
    def deadline(self):
        """Gets the deadline of this HotelProductCancellationPolicy.

        Represents the deadline after which the penalty applies. DateTime is in ISO 8601 [https://www.w3.org/TR/NOTE-datetime]. Example: 2010-08-14T12:00:00+01:00 Example: 2010-08-14T12:00:00Z Example: 2010-08-14T12:00:00-01:00 The value is expressed in the hotel local time zone, with the added time zone difference. So you can compute the deadline in UTC(GMT) if desired.

        :return: The deadline of this HotelProductCancellationPolicy.
        :rtype: datetime
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this HotelProductCancellationPolicy.

        Represents the deadline after which the penalty applies. DateTime is in ISO 8601 [https://www.w3.org/TR/NOTE-datetime]. Example: 2010-08-14T12:00:00+01:00 Example: 2010-08-14T12:00:00Z Example: 2010-08-14T12:00:00-01:00 The value is expressed in the hotel local time zone, with the added time zone difference. So you can compute the deadline in UTC(GMT) if desired.

        :param deadline: The deadline of this HotelProductCancellationPolicy.
        :type deadline: datetime
        """

        self._deadline = deadline

    @property
    def description(self):
        """Gets the description of this HotelProductCancellationPolicy.


        :return: The description of this HotelProductCancellationPolicy.
        :rtype: QualifiedFreeText
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HotelProductCancellationPolicy.


        :param description: The description of this HotelProductCancellationPolicy.
        :type description: QualifiedFreeText
        """

        self._description = description

    @property
    def number_of_nights(self):
        """Gets the number_of_nights of this HotelProductCancellationPolicy.

        Number of nights due as fee in case of cancellation.

        :return: The number_of_nights of this HotelProductCancellationPolicy.
        :rtype: int
        """
        return self._number_of_nights

    @number_of_nights.setter
    def number_of_nights(self, number_of_nights):
        """Sets the number_of_nights of this HotelProductCancellationPolicy.

        Number of nights due as fee in case of cancellation.

        :param number_of_nights: The number_of_nights of this HotelProductCancellationPolicy.
        :type number_of_nights: int
        """
        if number_of_nights is not None and number_of_nights < 0:
            raise ValueError("Invalid value for `number_of_nights`, must be a value greater than or equal to `0`")

        self._number_of_nights = number_of_nights

    @property
    def percentage(self):
        """Gets the percentage of this HotelProductCancellationPolicy.

        Percentage of the total stay amount to be paid in case of cancellation. Value is between 0 and 100.

        :return: The percentage of this HotelProductCancellationPolicy.
        :rtype: str
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this HotelProductCancellationPolicy.

        Percentage of the total stay amount to be paid in case of cancellation. Value is between 0 and 100.

        :param percentage: The percentage of this HotelProductCancellationPolicy.
        :type percentage: str
        """
        if percentage is not None and not re.search(r'^\\d+(\\.\\d+)?$', percentage):
            raise ValueError("Invalid value for `percentage`, must be a follow pattern or equal to `/^\\d+(\\.\\d+)?$/`")

        self._percentage = percentage

    @property
    def type(self):
        """Gets the type of this HotelProductCancellationPolicy.


        :return: The type of this HotelProductCancellationPolicy.
        :rtype: CancellationType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HotelProductCancellationPolicy.


        :param type: The type of this HotelProductCancellationPolicy.
        :type type: CancellationType
        """

        self._type = type
