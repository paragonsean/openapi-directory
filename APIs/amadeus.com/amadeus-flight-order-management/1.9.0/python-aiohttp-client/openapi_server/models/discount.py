# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.discount_traveler_type import DiscountTravelerType
from openapi_server.models.discount_type import DiscountType
import re
from openapi_server import util


class Discount(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, card_number: str=None, certificate_number: str=None, city_name: str=None, sub_type: DiscountType=None, traveler_type: DiscountTravelerType=None):
        """Discount - a model defined in OpenAPI

        :param card_number: The card_number of this Discount.
        :param certificate_number: The certificate_number of this Discount.
        :param city_name: The city_name of this Discount.
        :param sub_type: The sub_type of this Discount.
        :param traveler_type: The traveler_type of this Discount.
        """
        self.openapi_types = {
            'card_number': str,
            'certificate_number': str,
            'city_name': str,
            'sub_type': DiscountType,
            'traveler_type': DiscountTravelerType
        }

        self.attribute_map = {
            'card_number': 'cardNumber',
            'certificate_number': 'certificateNumber',
            'city_name': 'cityName',
            'sub_type': 'subType',
            'traveler_type': 'travelerType'
        }

        self._card_number = card_number
        self._certificate_number = certificate_number
        self._city_name = city_name
        self._sub_type = sub_type
        self._traveler_type = traveler_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Discount':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Discount of this Discount.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def card_number(self):
        """Gets the card_number of this Discount.

        resident card number

        :return: The card_number of this Discount.
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this Discount.

        resident card number

        :param card_number: The card_number of this Discount.
        :type card_number: str
        """
        if card_number is not None and not re.search(r'[0-9A-Z][0-9]{0,12}[A-Z]', card_number):
            raise ValueError("Invalid value for `card_number`, must be a follow pattern or equal to `/[0-9A-Z][0-9]{0,12}[A-Z]/`")

        self._card_number = card_number

    @property
    def certificate_number(self):
        """Gets the certificate_number of this Discount.

        resident certificate number

        :return: The certificate_number of this Discount.
        :rtype: str
        """
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, certificate_number):
        """Sets the certificate_number of this Discount.

        resident certificate number

        :param certificate_number: The certificate_number of this Discount.
        :type certificate_number: str
        """
        if certificate_number is not None and not re.search(r'[0-9A-Z][0-9]{0,12}[A-Z]', certificate_number):
            raise ValueError("Invalid value for `certificate_number`, must be a follow pattern or equal to `/[0-9A-Z][0-9]{0,12}[A-Z]/`")

        self._certificate_number = certificate_number

    @property
    def city_name(self):
        """Gets the city_name of this Discount.

        city of residence

        :return: The city_name of this Discount.
        :rtype: str
        """
        return self._city_name

    @city_name.setter
    def city_name(self, city_name):
        """Sets the city_name of this Discount.

        city of residence

        :param city_name: The city_name of this Discount.
        :type city_name: str
        """

        self._city_name = city_name

    @property
    def sub_type(self):
        """Gets the sub_type of this Discount.


        :return: The sub_type of this Discount.
        :rtype: DiscountType
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this Discount.


        :param sub_type: The sub_type of this Discount.
        :type sub_type: DiscountType
        """

        self._sub_type = sub_type

    @property
    def traveler_type(self):
        """Gets the traveler_type of this Discount.


        :return: The traveler_type of this Discount.
        :rtype: DiscountTravelerType
        """
        return self._traveler_type

    @traveler_type.setter
    def traveler_type(self, traveler_type):
        """Sets the traveler_type of this Discount.


        :param traveler_type: The traveler_type of this Discount.
        :type traveler_type: DiscountTravelerType
        """

        self._traveler_type = traveler_type
